import graphene

from backend.apps.types import ProvinciaType
from backend.apps.core.models import Provincia, PresupuestoGlobal, PresupuestoCentral, ListadoProvincia


class InsertData(graphene.Mutation):
    status = graphene.String()
    province_data = graphene.Field(ProvinciaType)

    class Arguments:
        dpa = graphene.String(required=True)
        nombre = graphene.String(required=True)
        enviado_a = graphene.String(required=True)
        mes = graphene.String(required=True)
        anno = graphene.String(required=True)
        enviado_esta_semana = graphene.Boolean(required=True)

        # presupuesto global relacion
        pg_real_mes = graphene.Float(required=True)
        pg_real_acomulado = graphene.Float(required=True)
        pg_estimado_mes = graphene.Float(required=True)
        pg_estimado_cierre_anno = graphene.Float()

        # presupuesto central relacion
        pc_real_mes = graphene.Float(required=True)
        pc_real_acomulado = graphene.Float(required=True)
        pc_estimado_mes = graphene.Float(required=True)
        pc_estimado_cierre_anno = graphene.Float()

    def mutate(self, info, dpa, nombre, enviado_a, mes, anno, enviado_esta_semana, pg_real_mes, pg_real_acomulado,
               pg_estimado_mes, pg_estimado_cierre_anno, pc_real_mes, pc_real_acomulado, pc_estimado_mes,
               pc_estimado_cierre_anno):

        presupuesto_global = PresupuestoGlobal.objects.create(
            pg_real_mes=pg_real_mes,
            pg_real_acomulado=pg_real_acomulado,
            pg_estimado_mes=pg_estimado_mes,
            pg_estimado_cierre_anno=pg_estimado_cierre_anno
        )
        presupuesto_central = PresupuestoCentral.objects.create(
            pc_real_mes=pc_real_mes,
            pc_real_acomulado=pc_real_acomulado,
            pc_estimado_mes=pc_estimado_mes,
            pc_estimado_cierre_anno=pc_estimado_cierre_anno
        )
        province_data = Provincia.objects.create(
            dpa=dpa,
            nombre=nombre,
            enviado_a=enviado_a,
            mes=mes,
            anno=anno,
            enviado_esta_semana=enviado_esta_semana,
            presupuesto_global=presupuesto_global,
            presupuesto_central=presupuesto_central
        )
        province_data.save()
        update_province = ListadoProvincia.objects.get(nombre=nombre)
        update_province.actualizado = True
        update_province.save()
        return InsertData(status='ok', province_data=province_data)
