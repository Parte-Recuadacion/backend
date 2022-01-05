import graphene

from backend.apps.types import ProvinciaType
from backend.apps.core.models import Provincia


class getProvinceData(graphene.Mutation):
    status = graphene.String()
    province = graphene.List(ProvinciaType)

    class Arguments:
        mes = graphene.String(required=True)
        anno = graphene.String(required=True)
        provincia = graphene.String(required=True)

    def mutate(self, info, provincia, mes, anno):
        global province
        province = Provincia.objects.filter(nombre=provincia, mes=mes, anno=anno)
        return getProvinceData(status='ok', province=province)