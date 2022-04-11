from graphene_django.types import DjangoObjectType
from backend.apps.core import models


class ListadoProvinciaType(DjangoObjectType):
    class Meta:
        model = models.ListadoProvincia


class ProvinciaType(DjangoObjectType):
    class Meta:
        model = models.Provincia


class PresupuestoCentralType(DjangoObjectType):
    class Meta:
        model = models.PresupuestoCentral


class PresupuestoSeguridadSocialType(DjangoObjectType):
    class Meta:
        model = models.PresupuestoSeguridadSocial


class PresupuestoLocalType(DjangoObjectType):
    class Meta:
        model = models.PresupuestoLocal
