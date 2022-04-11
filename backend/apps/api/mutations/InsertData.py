import graphene
from backend.apps.types import ProvinciaType
from backend.apps.core.models import Provincia, PresupuestoCentral, PresupuestoSeguridadSocial, PresupuestoLocal, \
    ListadoProvincia


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

        # presupuesto central relacion
        central_plan_mes = graphene.Float(required=True)
        central_plan_acumulado = graphene.Float(required=True)
        central_real_mes = graphene.Float(required=True)
        central_real_acumulado = graphene.Float(required=True)
        central_estimado_mes = graphene.Float(required=True)
        central_estimado_acumulado = graphene.Float(required=True)

        # presupuesto seguridad social relacion
        social_plan_mes = graphene.Float(required=True)
        social_plan_acumulado = graphene.Float(required=True)
        social_real_mes = graphene.Float(required=True)
        social_real_acumulado = graphene.Float(required=True)
        social_estimado_mes = graphene.Float(required=True)
        social_estimado_acumulado = graphene.Float(required=True)

        # presupuesto local
        local_plan_mes = graphene.Float()
        local_plan_acumulado = graphene.Float()
        local_real_mes = graphene.Float()
        local_real_acumulado = graphene.Float()
        local_estimado_mes = graphene.Float()
        local_estimado_acumulado = graphene.Float()

    def mutate(self, info, dpa, nombre, enviado_a, mes, anno, enviado_esta_semana,
               central_plan_mes,
               central_plan_acumulado,
               central_real_mes,
               central_real_acumulado,
               central_estimado_mes,
               central_estimado_acumulado,
               social_plan_mes,
               social_plan_acumulado,
               social_real_mes,
               social_real_acumulado,
               social_estimado_mes,
               social_estimado_acumulado,
               local_plan_mes,
               local_plan_acumulado,
               local_real_mes,
               local_real_acumulado,
               local_estimado_mes,
               local_estimado_acumulado
               ):
        presupuesto_central = PresupuestoCentral.objects.create(
            central_plan_mes=central_plan_mes,
            central_plan_acumulado=central_plan_acumulado,
            central_real_mes=central_real_mes,
            central_real_acumulado=central_real_acumulado,
            central_estimado_mes=central_estimado_mes,
            central_estimado_acumulado=central_estimado_acumulado
        )
        presupuesto_seguridad_social = PresupuestoSeguridadSocial.objects.create(
            social_plan_mes=social_plan_mes,
            social_plan_acumulado=social_plan_acumulado,
            social_real_mes=social_real_mes,
            social_real_acumulado=social_real_acumulado,
            social_estimado_mes=social_estimado_mes,
            social_estimado_acumulado=social_estimado_acumulado,
        )
        presupuesto_local = PresupuestoLocal.objects.create(
            local_plan_mes=local_plan_mes,
            local_plan_acumulado=local_plan_acumulado,
            local_real_mes=local_real_mes,
            local_real_acumulado=local_real_acumulado,
            local_estimado_mes=local_estimado_mes,
            local_estimado_acumulado=local_estimado_acumulado,
        )
        province_data = Provincia.objects.create(
            dpa=dpa,
            nombre=nombre,
            enviado_a=enviado_a,
            mes=mes,
            anno=anno,
            enviado_esta_semana=enviado_esta_semana,
            presupuesto_central=presupuesto_central,
            presupuesto_seguridad_social=presupuesto_seguridad_social,
            presupuesto_local=presupuesto_local,
        )
        province_data.save()
        update_province = ListadoProvincia.objects.get(nombre=nombre)
        update_province.actualizado = True
        update_province.save()
        return InsertData(status='ok', province_data=province_data)
