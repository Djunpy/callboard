from django.db import models

from advert.models import AdvertAbstract, CommonConditionChoice, Brand


class MaterialType(models.Model):
    """"""

    material_type = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name = 'Тип материалов для строительства'
        verbose_name_plural = 'Тип материалов для строительства'


class BuildingMaterials(AdvertAbstract, CommonConditionChoice):
    """Строительные материалы"""

    material_type = models.ForeignKey(MaterialType, on_delete=models.CASCADE, verbose_name='Тип материала')

    class Meta(AdvertAbstract.Meta, CommonConditionChoice.Meta):
        verbose_name = 'Стройматериал'
        verbose_name_plural = 'Стройматериалы'


class Tool(AdvertAbstract, CommonConditionChoice):
    """Газовое и сварочное оборудование"""

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True, related_name='%(app_label)s_%(class)s_electronics')

    class Meta(AdvertAbstract.Meta, CommonConditionChoice.Meta):
        verbose_name = 'Стройматериал'
        verbose_name_plural = 'Стройматериалы'
