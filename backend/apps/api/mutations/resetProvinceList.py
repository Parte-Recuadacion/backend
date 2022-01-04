import graphene

from backend.apps.types import ListadoProvinciaType
from backend.apps.core.models import ListadoProvincia


class resetProvinceList(graphene.Mutation):
    status = graphene.String()

    def mutate(self, info,):
        province = ListadoProvincia.objects.all().delete()
        list = ListadoProvincia.objects.create(dpa=2100, nombre="Pinar del Río", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2200, nombre="Artemisa", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2300, nombre="La Habana", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2400, nombre="Mayabeque", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2500, nombre="Matanzas", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2600, nombre="Villa Clara", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2700, nombre="Cienfuegos", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2800, nombre="Santic Spiritus", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=2900, nombre="Ciego de Ávila", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=3000, nombre="Camagüey", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=3100, nombre="Las Tunas", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=3200, nombre="Holguín", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=3300, nombre="Granma", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=3400, nombre="Santiago de Cuba", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=3500, nombre="Guantánamo", actualizado=False)
        list.save()
        list = ListadoProvincia.objects.create(dpa=4000, nombre="Isla de la Juventud", actualizado=False)
        list.save()

        return resetProvinceList(status='ok')