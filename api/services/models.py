from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from advert.models import AdvertAbstract


class ServiceType(models.Model):

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Тип услуги'


class Service(AdvertAbstract):

    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name='Тип услуги')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

