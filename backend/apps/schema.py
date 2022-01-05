import graphene
from graphene_django.types import ObjectType
from backend.apps.api.mutations import getProvinceData, InsertData, resetProvinceList, resetProvince
from backend.apps.api.queries.province import getProvinceMissing
from backend.apps.types import ProvinciaType, PresupuestoCentralType, PresupuestoGlobalType


class Mutation(
    ObjectType
):
    province_data = getProvinceData.getProvinceData.Field()
    insert_data = InsertData.InsertData.Field()
    reset_list = resetProvinceList.resetProvinceList.Field()
    reset_province = resetProvince.resetProvince.Field()


class Query(getProvinceMissing, ObjectType): pass


types = [ProvinciaType, PresupuestoCentralType, PresupuestoGlobalType]

schema = graphene.Schema(query=Query, mutation=Mutation, types=types)
