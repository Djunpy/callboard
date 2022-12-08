from django.db import models

from advert.models import AdvertAbstract


class CommonProperty(models.Model):
    REPAIR = (
        ('required', 'Требуется'), ('cosmetic', 'Косметический'),
        ('euro', 'Евро'), ('disigner', 'Дизайнерский')
    )

    repair = models.CharField(max_length=15, choices=REPAIR, default='design', verbose_name='Ремонт')
    floor_in_house = models.SmallIntegerField(verbose_name='Этажей в доме')
    tv = models.BooleanField(default=False, verbose_name='Телевидение')
    internet = models.BooleanField(default=False, verbose_name='Интернет')


    class Meta:
        abstract = True


class Flat(AdvertAbstract, CommonProperty):

    HOUSE_TYPE = (
        ('brick', 'Кирпичный'), ('panel', 'Панельный'),
        ('blocky', 'Блочный'), ('monolit', 'Монолитный'),
        ('monolit-brick', 'Монолитно-Кирпичный'), ('wood', 'Деревянный')
    )

    PARKING = (
        ('under', 'Подземная'), ('yarn', 'Открытая во дворе'),
        ('garage', 'Гараж')
    )

    HOUSING_STOCK = (
        ('primary', 'Первичка'), ('resale', 'Вторичка')
    )

    BATHROOM = (
        ('combined', 'Совмещенный'), ('divided', 'Разделенный')
    )



    TYPE_OFFER = (
        ('sell', 'Продать'), ('pass', 'Сдать')
    )

    floor = models.SmallIntegerField(verbose_name='Этаж')
    house_type = models.CharField(max_length=20, choices=HOUSE_TYPE, default='brick', verbose_name='Тип дома')
    parking = models.CharField(max_length=15, choices=PARKING, default='yard')
    housing_stock = models.CharField(max_length=10, choices=HOUSING_STOCK, default='primary', verbose_name='Жилой фонд')
    balcony = models.BooleanField(default=False, verbose_name='Балкон')
    loggia = models.BooleanField(default=False, verbose_name='Лоджия')
    bathroom = models.CharField(max_length=10, choices=BATHROOM, default='divided', verbose_name='Тип санузла')
    furniture_kitchen = models.BooleanField(default=False, verbose_name='Кухонная мебель')
    furniture_clothes_places = models.BooleanField(default=False, verbose_name='Мебель для хранения одежды')
    furniture_sleeping_places = models.BooleanField(default=False, verbose_name='Спальные места')
    washing_machine = models.BooleanField(default=False, verbose_name='Стиральная машина')
    dishwasher = models.BooleanField(default=False, verbose_name='Посудомоечная машина')
    total_area = models.FloatField(verbose_name='Общая площадь')
    living_space = models.FloatField(verbose_name='Жилая площадь')
    number_of_rooms = models.SmallIntegerField(verbose_name='Количество комнат')
    ceiling_height = models.FloatField(verbose_name='Высота потолков')
    type_offer = models.CharField(max_length=10, choices=TYPE_OFFER, default='sell', verbose_name='Тип предложения')
    conditioner = models.BooleanField(default=False, verbose_name='Кондиционер')
    fridge = models.BooleanField(default=False, verbose_name='Холодильник')
    elevator = models.BooleanField(default=False, verbose_name='Лифт')

    class Meta(AdvertAbstract.Meta, CommonProperty.Meta):
        verbose_name = 'Квартиры и комнаты'
        verbose_name_plural = 'Квартиры и комнаты'


class House(AdvertAbstract, CommonProperty):

    TYPE_HOUSE = (
        ('house', 'Дом'), ('dacha', 'Дача'),
        ('cottage', 'Котедж'), ('townhouse', 'Таунхаус')
    )

    WALL_MATERIAL = (
        ('brick', 'Кирпич'), ('timber', 'Брус'),
        ('log', 'Брус'), ('metal', 'Металл'),
        ('gasblock', 'Газоблоки'), ('penoblock', 'Пеноблоки')
    )

    PARKING = (
        ('no', 'Нет'), ('garage', 'Гараж'),
        ('parkingspace', 'Парковочное место')
    )

    parking = models.CharField(max_length=15, choices=PARKING, default='no')
    type_house = models.CharField(max_length=15, choices=TYPE_HOUSE, default='dacha', verbose_name='Вид объекта')
    wall_material = models.CharField(max_length=15, choices=WALL_MATERIAL, default='brick', verbose_name='Материал стен')
    bath = models.BooleanField(default=False, verbose_name='Баня')
    poll = models.BooleanField(default=False, verbose_name='бассейн')
    year_of_construction = models.SmallIntegerField(verbose_name='Год постройкпи')
    number_of_rooms = models.SmallIntegerField(verbose_name='Количество комнат')
    house_area = models.FloatField(verbose_name='Площадь дома')
    land_area = models.FloatField(verbose_name='Площадь участка')
    bathroom_street = models.BooleanField(default=False, verbose_name='Санузел на улице')
    bathroom_house = models.BooleanField(default=False, verbose_name='Санузел в доме')
    asphalt_road = models.BooleanField(default=False, verbose_name='Асфальтированная дорога')
    public_transport = models.BooleanField(default=False, verbose_name='Остановка общественного транспорта ')
    pharmacy = models.BooleanField(default=False, verbose_name='Аптека')
    shop = models.BooleanField(default=False, verbose_name='Магазин')
    kindergarten = models.BooleanField(default=False, verbose_name='Детский сад')


    class Meta(AdvertAbstract.Meta, CommonProperty.Meta):
        verbose_name = 'Дома и дачи'
        verbose_name_plural = 'Дома и дачи'


class Plot(AdvertAbstract):

    TYPE_PLOT = (
        ('agriculture', 'Под сельское хозяйство'),
        ('construction', 'Под строительство')
    )

    type_plot = models.CharField(max_length=15, choices=TYPE_PLOT, default='agriculture', verbose_name='Тип участка')
    land_area = models.FloatField(verbose_name='Площадь земли')
    gas = models.BooleanField(default=False, verbose_name='Газофикация')
    water_supply = models.BooleanField(default=False, verbose_name='Водоснабжение')
    sewerage = models.BooleanField(default=False, verbose_name='Канализация')
    power_supply = models.BooleanField(default=False, verbose_name='Электроснабжение')

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'