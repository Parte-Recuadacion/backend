from django.contrib import admin

from backend.apps.core.models import Provincia, ListadoProvincia, PresupuestoCentral, PresupuestoGlobal


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'dpa',
        'nombre',
        'enviado_a',
        'enviado_esta_semana',
        'mes',
        'anno'
    )


# @admin.register(ListadoProvincia)
# class ListadoProvinciaAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'dpa',
#         'nombre',
#         'actualizado'
#     )


@admin.register(PresupuestoGlobal)
class PresupuestoGlobalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pg_real_mes',
        'pg_real_acomulado',
        'pg_estimado_mes',
        'pg_estimado_cierre_anno'
    )


@admin.register(PresupuestoCentral)
class PresupuestoGlobalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pc_real_mes',
        'pc_real_acomulado',
        'pc_estimado_mes',
        'pc_estimado_cierre_anno'
    )


def update_province_true(self, request, queryset):
    queryset.update(actualizado=True)


update_province_true.short_description = "Poner provincia en actualizado"


def update_province_false(self, request, queryset):
    queryset.update(actualizado=False)


update_province_false.short_description = "Poner provincia en no actualizado"


class ListadoProvinciaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'dpa',
        'nombre',
        'actualizado'
    )
    actions = [update_province_true, update_province_false]
    ordering = ['dpa']


admin.site.register(ListadoProvincia, ListadoProvinciaAdmin)
