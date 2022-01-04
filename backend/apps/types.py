from graphene_django.types import DjangoObjectType
from backend.apps.core import models


class ListadoProvinciaType(DjangoObjectType):
    class Meta:
        model = models.ListadoProvincia


class ProvinciaType(DjangoObjectType):
    class Meta:
        model = models.Provincia


class PresupuestoGlobalType(DjangoObjectType):
    class Meta:
        model = models.PresupuestoGlobal


class PresupuestoCentralType(DjangoObjectType):
    class Meta:
        model = models.PresupuestoCentral
