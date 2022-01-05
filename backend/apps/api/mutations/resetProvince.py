import graphene

from backend.apps.types import ListadoProvinciaType
from backend.apps.core.models import ListadoProvincia


class resetProvince(graphene.Mutation):
    status = graphene.String()

    class Arguments:
        dpa = graphene.String(required=True)

    def mutate(self, info, dpa):
        province = ListadoProvincia.objects.get(dpa=dpa)
        province.actualizado = True
        province.save()
        return resetProvince(status='ok')
