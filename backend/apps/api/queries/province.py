import graphene
from graphql import GraphQLError

from backend.apps.types import ListadoProvinciaType
from backend.apps.core.models import ListadoProvincia


class getProvinceMissing(graphene.ObjectType):
    province_missing = graphene.List(ListadoProvinciaType)

    def resolve_province_missing(self, info):
        return ListadoProvincia.objects.filter(actualizado=False)
