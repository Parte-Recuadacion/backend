from cachecontrol import cache
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def set_cache(self):
        from cachecontrol import cache
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class CreatedUpdatedModel(models.Model):
    """
    A model to reuse the `created_at` and `updated_at` fields
    """
    created_at = models.DateTimeField(default=now, null=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = now()
        super().save(*args, **kwargs)

    @property
    def is_new(self):
        return self.created_at <= (now() - timedelta(days=1))


class DeletedModel(models.Model):
    """
    A model to reuse the `updated_at` field
    """

    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def safe_delete(self):
        self.deleted_at = now()
        self.save()


class PresupuestoCentral(models.Model):
    central_plan_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    central_plan_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    central_real_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    central_real_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    central_estimado_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    central_estimado_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)

    class Meta:
        db_table = 'presupuesto_central'
        verbose_name = 'presupuesto_central'
        verbose_name_plural = 'presupuestos_centrales'


class PresupuestoSeguridadSocial(models.Model):
    social_plan_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    social_plan_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    social_real_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    social_real_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    social_estimado_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    social_estimado_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)

    class Meta:
        db_table = 'presupuesto_social'
        verbose_name = 'presupuesto_social'
        verbose_name_plural = 'presupuestos_sociales'


class PresupuestoLocal(models.Model):
    local_plan_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    local_plan_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    local_real_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    local_real_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    local_estimado_mes = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)
    local_estimado_acumulado = models.DecimalField(max_digits=25, blank=True, null=True, decimal_places=1)

    class Meta:
        db_table = 'presupuesto_local'
        verbose_name = 'presupuesto_local'
        verbose_name_plural = 'presupuestos_locales'


class Provincia(models.Model):
    presupuesto_central = models.ForeignKey(PresupuestoCentral, on_delete=models.CASCADE,
                                            verbose_name='Presupuesto Central', null=True)

    presupuesto_seguridad_social = models.ForeignKey(PresupuestoSeguridadSocial, on_delete=models.CASCADE,
                                                     verbose_name='Presupuesto Seguridad Social', null=True)

    presupuesto_local = models.ForeignKey(PresupuestoLocal, on_delete=models.CASCADE,
                                          verbose_name='Presupuesto Local', null=True)

    dpa = models.CharField(max_length=4, null=True, blank=True)
    nombre = models.CharField(max_length=25)
    enviado_a = models.DateTimeField(null=True, blank=True)
    mes = models.CharField(max_length=25, null=True, blank=True)
    anno = models.CharField(max_length=4, null=True, blank=True)
    enviado_esta_semana = models.BooleanField(default=False)

    class Meta:
        db_table = 'provincia'
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'


class ListadoProvincia(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    nombre = models.CharField(max_length=25)
    actualizado = models.BooleanField(default=False)

    class Meta:
        db_table = 'listado_provincia'
        verbose_name = 'listado_provincia'
        verbose_name_plural = 'listado_provincias'
