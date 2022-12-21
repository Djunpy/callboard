from django.db import models

from advert.models import Brand, AdvertAbstract, Color


class SizeThing(models.Model):
    """Размеры вещей"""

    size = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Размер одежды'
        verbose_name_plural = 'Размеры одежды'


class CommonThing(models.Model):
    """Общие поля для вещей"""

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Бренд одежды')
    size = models.ForeignKey(SizeThing, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Размер одежды',
                             related_name="%(app_label)s_%(class)s_things")
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет',
                              related_name="%(app_label)s_%(class)s_things")

    class Meta:
        abstract = True

class Thing(AdvertAbstract, CommonThing):
    """Вещи"""

    class Meta(AdvertAbstract.Meta, CommonThing.Meta):
        verbose_name = 'Личная вещ'
        verbose_name_plural = 'Личные вещи'


class Jewel(AdvertAbstract, CommonThing):
    """Драгоценность"""

    diamond = models.BooleanField(default=False, verbose_name='Бриллиант')
    cubic_zirconia = models.BooleanField(default=False, verbose_name='Фианит')
    sapphire = models.BooleanField(default=False, verbose_name='Cапфир')
    emerald = models.BooleanField(default=False, verbose_name='Изумруд')
    pearl = models.BooleanField(default=False, verbose_name='Жемчуг')
    topaz = models.BooleanField(default=False, verbose_name='Топаз')
    amethyst = models.BooleanField(default=True, verbose_name='Аметист')
    amber = models.BooleanField(default=False, verbose_name='Янтарь')
    ruby = models.BooleanField(default=False, verbose_name='Рубин')
    alexandrite = models.BooleanField(default=False, verbose_name='Александрит')
    pomegranate = models.BooleanField(default=False, verbose_name='Гранат')
    without_inserts = models.BooleanField(default=False, verbose_name='Без вставок')
    placer = models.BooleanField(default=False, verbose_name='Россыпь камней')
    stone_number = models.SmallIntegerField(blank=True, null=True, verbose_name='Количество камней')

    class Meta(AdvertAbstract.Meta, CommonThing.Meta):
        verbose_name = 'Драгоценность'
        verbose_name_plural = 'Драгоценности'


class ClockType(models.Model):
    """Тип часов"""

    clock_type = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'Тип часов'
        verbose_name_plural = 'Типы Часов'


class Clock(AdvertAbstract):
    """Часы"""

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Бренд')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет часов')
    clock_type = models.ForeignKey(ClockType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип часов')

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'


class BijouterieType(models.Model):
    """Тип бижутерии"""

    bijouterie_type = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = 'Тип бижутерии'
        verbose_name_plural = 'Тип бижутерии'


class Bijouterie(AdvertAbstract):
    """Бижутерия"""

    FOR_WHOM = (
        ('women', 'Женщины'), ('men', 'Мужчины'),
        ('unisex', 'Унисекс'), ('girls', 'Девочки'),
        ('boys', 'Мальчики')
    )

    for_whom = models.CharField(max_length=10, choices=FOR_WHOM, verbose_name='Для кого')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Бренд бижутерии')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет')
    bijouterie_type = models.ForeignKey(BijouterieType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип бижутерии')

    class Meta:
        verbose_name = 'Бижутерия'
        verbose_name_plural = 'Бижутерии'

