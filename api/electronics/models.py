from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from advert.models import AdvertAbstract, Color


class ElectronicType(MPTTModel):

    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Тип электроники'
        verbose_name_plural = 'Типы электроники'


class ElectronicAbstract(models.Model):
    """Общая модель электроники"""

    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет электроники')
    electronic_type = models.ForeignKey(ElectronicType, on_delete=models.CASCADE)
    brand = models.ForeignKey('advert.Brand', on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_electronics")
    type_brand = models.ForeignKey('advert.Brand', on_delete=models.CASCADE,
                              related_name="%(app_label)s_%(class)s_electronics_type")

    class Meta:
        abstract = True


class Processor(models.Model):
    """Процессоры для ноутбуков/компьютеров"""

    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'


class VideoCardLaptop(models.Model):
    """Видеокарты для ноутбуков/компьютеров"""

    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'


class LaptopAndComputer(AdvertAbstract, ElectronicAbstract):
    """Компьютеры/Ноутбуки"""

    cpu = models.ForeignKey(Processor, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Процессор')
    video_card = models.ForeignKey(VideoCardLaptop, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Видеоката')
    diagonal = models.FloatField(blank=True, null=True, verbose_name='Диагональ экрана')
    screen_resolution = models.CharField(max_length=20, blank=True, null=True, verbose_name='Разрешение экрана')
    screen_refresh = models.SmallIntegerField(blank=True, null=True, verbose_name='Частота обновления экрана')
    monitor = models.BooleanField(default=False, blank=True, null=True, verbose_name='Наличие монитора')
    storage_capacity = models.SmallIntegerField(blank=True, null=True, verbose_name='Объем накопителя HDD/SDD')
    sdd = models.BooleanField(default=False)
    hdd = models.BooleanField(default=True)
    ram = models.SmallIntegerField(blank=True, null=True, verbose_name='Оперативная карта')
    weight = models.FloatField(blank=True, null=True, verbose_name='Вес')


    class Meta(AdvertAbstract.Meta, ElectronicAbstract.Meta):
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'


class Phone(AdvertAbstract, ElectronicAbstract):
    """Телефоны/Планшеты"""

    memory = models.SmallIntegerField(blank=True, null=True, verbose_name='Встроенная память')
    ram = models.SmallIntegerField(blank=True, null=True, verbose_name='Оперативная карта')


    class Meta(AdvertAbstract.Meta, ElectronicAbstract.Meta):
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class OtherElectronic(AdvertAbstract):
    """Прочая электроника"""

    class Meta:
        verbose_name = 'Другая электроника'
        verbose_name_plural = 'Другая электроника'
