import graphene
from backend.apps.core.models import ListadoProvincia


class resetProvinceList(graphene.Mutation):
    status = graphene.String()

    def mutate(self, info,):
        province = ListadoProvincia.objects.all()
        for provincias in province:
            provincias.actualizado = False
            provincias.save()
        return resetProvinceList(status='ok')