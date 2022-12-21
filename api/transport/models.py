from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from advert.models import AdvertAbstract, Color, Condition


class TransportBrand(MPTTModel):

    name = models.CharField(max_length=80, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class TransportBodyType(models.Model):
    body_type = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузовы'


class CommonTransport(models.Model):
    """Общие поля для разных видов транспортов"""

    color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Цвет транспорта')
    brand = models.ForeignKey('advert.Brand', on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_transport")
    type_brand = models.ForeignKey('advert.Brand', on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_transport_type")
    discount = models.ForeignKey('advert.Discount', on_delete=models.CASCADE,
                                 blank=True, null=True,  related_name="%(app_label)s_%(class)s_transport")

    class Meta:
        abstract = True



class OperationHistory(models.Model):
    """История эксплуатации и состояние"""

    CONDITION_2 = (
        ('n', 'Новый'), ('pr', 'С пробегом')
    )

    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name='Состояние транспорта')
    condition_2 = models.CharField(max_length=2, choices=CONDITION_2, default='n')

    mileage = models.CharField(max_length=50, blank=True, null=True, verbose_name='Пробег')
    owners = models.SmallIntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    class Meta:
        abstract = True


class MultimediaAndNavigation(models.Model):
    """Мультимедиа и навигация"""

    cd_dvd = models.BooleanField(default=False, verbose_name='CD/DVD')
    mp3 = models.BooleanField(default=False, verbose_name='MP3')
    radio = models.BooleanField(default=False, verbose_name='Радио')
    video = models.BooleanField(default=False, verbose_name='Видео')
    usb = models.BooleanField(default=False)
    aux = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    gps = models.BooleanField(default=False, verbose_name='GPS-Навигация')

    class Meta:
        abstract = True

class DrivingAssistance(models.Model):
    """Помощь при вождении"""

    automatic_valet = models.BooleanField(default=False, verbose_name='Автоматический парковщик')
    rain_sensor = models.BooleanField(default=False, verbose_name='Датчик дождя')
    light_sensor = models.BooleanField(default=False, verbose_name='Датчик света')
    front_parking_sensors = models.BooleanField(default=False, verbose_name='Парктроник передний')
    rear_parking_sensors = models.BooleanField(default=False, verbose_name='Парктроник задний')
    blind_spot_monitor = models.BooleanField(default=False, verbose_name='Система контроля слепых зон')
    rear_view_camera = models.BooleanField(default=False, verbose_name='Камера заднего вида')
    cruise_control = models.BooleanField(default=False, verbose_name='Круиз контроль')
    on_board_computer = models.BooleanField(default=False, verbose_name='Бортовый компьютер ')

    class Meta:
        abstract = True


class AntiTheftSystem(models.Model):
    """Противоугонная система"""

    signaling = models.BooleanField(default=False, verbose_name='Сигнализация')
    central_locking = models.BooleanField(default=False, verbose_name='Центральный замок')
    satellite = models.BooleanField(default=False, verbose_name='Спутник')
    immobilizer = models.BooleanField(default=False, verbose_name='Иммобилайзер')

    class Meta:
        abstract = True


class Airbags(models.Model):
    """Подушки безопасности"""

    frontal = models.BooleanField(default=False, verbose_name='Фронтальные')
    knees = models.BooleanField(default=False, verbose_name='Колленые ')
    curtains = models.BooleanField(default=False, verbose_name='Шторки')
    side_front = models.BooleanField(default=False, verbose_name='Боковые передние ')
    side_rear = models.BooleanField(default=False, verbose_name='Боковые задние ')

    class Meta:
        abstract = True


class ActiveSafety(models.Model):

    """Активная безопасность"""

    anti_lock_brakes = models.BooleanField(default=False, verbose_name='Антиблокировка тормозов')
    anti_slip = models.BooleanField(default=False, verbose_name='Антиблокировка')
    exchange_rate_stability = models.BooleanField(default=False, verbose_name='Курсовая устойчивость')
    decay_of_braking_forces = models.BooleanField(default=False, verbose_name='Распад тормозных усилий')
    emergency_braking = models.BooleanField(default=False, verbose_name='Экстренное  торможение ')
    differential_block = models.BooleanField(default=False, verbose_name='Блок дифференциала')
    pedestrian_detection = models.BooleanField(default=False, verbose_name='Обнаружение пешеходов')

    class Meta:
        abstract = True


class Car(
    OperationHistory, MultimediaAndNavigation,
    DrivingAssistance, AntiTheftSystem,
    Airbags, ActiveSafety, AdvertAbstract,
    CommonTransport,
):
    SALOM = (
        ('leather', 'Кожа'), ('textile', 'Ткань'),
        ('velours', 'Велюр'), ('combined', 'Комбинированный')
    )

    POWER_STEERING = (
        ('hydrlic', 'Гидравлический'), ('electric', 'Электрический'),
        ('eltro-hyrlic', 'Электрогидравлический')
    )

    CLIMAT_CONTROL = (
        ('aircontr', 'Кондиционер'),
        ('climcondis', 'Климат-контроль одноразовый'),
        ('climconreus', 'Климат-контроль одноразовый')
    )

    POWER_WINDOWS = (
        ('fronly', 'Только передняя'), ('froandrear', 'Переднее и задние')
    )

    TYPE_ENGINE = (
        ('p', 'Бензин'), ('g', 'Газ'),
        ('d', 'Дизель'), ('gb', 'гибридные'),
        ('e', 'Электро')
    )

    TYPE_TRANSMISSION = (
        ('a', 'Автоматическая'),
        ('m', 'Механическая'),
        ('v', 'Вариативная'),
        ('r', 'Роботизированная')
    )

    DRIVE_UNIT = (
        ('front', 'Передний'), ('real', 'Задний'),
        ('full', 'Полный'), ('hybrid', 'Гибридный')
    )

    AUDIO_SYSTEM = (
        ('1', '2 Колонки'), ('2', '4 Колонки'),
        ('3', '6 Колонки'), ('1', '+8 Колонки')
    )

    HEADLIGHTS = (
        ('halogen', 'Галогенные'), ('xenon', 'Ксеноновые '),
        ('led', 'Светодиодные')
    )

    front_seats = models.BooleanField(default=False, verbose_name='Передних сидений')
    rear_seats = models.BooleanField(default=False, verbose_name='Задних сидений')
    mirror = models.BooleanField(default=False, verbose_name='Зеркал')
    steering_columns = models.BooleanField(default=False, verbose_name='Рулевые колонки')
    front_seats = models.BooleanField(default=False, verbose_name='Передние сиденья')
    rear_seats = models.BooleanField(default=False, verbose_name='Заднее сиденье')
    mirror = models.BooleanField(default=False, verbose_name='Зеркал')
    steering_column = models.BooleanField(default=False, verbose_name='Рулевой колонки')
    folding_mirrors = models.BooleanField(default=False, verbose_name='Складывание зеркал')
    salom = models.CharField(max_length=20, choices=SALOM, null=True, blank=True)
    power_steering = models.CharField(max_length=20, choices=POWER_STEERING, blank=True, null=True,
                                      verbose_name='Усилитель руля')
    climat_control = models.CharField(max_length=15, choices=CLIMAT_CONTROL,
                                      blank=True, null=True, verbose_name='Управление климатом')
    steering_wheel_control = models.BooleanField(default=True, verbose_name='Управление на руле')
    athermal_glazing = models.BooleanField(null=True, blank=True, verbose_name='Атермальный остекление')
    power_windows = models.CharField(max_length=20, choices=POWER_WINDOWS, blank=True, null=True,
                                     verbose_name='Электростеклоподъемники')
    type_engine = models.CharField(max_length=2, choices=TYPE_ENGINE, default='p', verbose_name='Тип двигателя')
    engine_volume = models.FloatField(max_length=10, blank=True, null=True, verbose_name='Обьем двигателя')
    power = models.SmallIntegerField(blank=True, null=True, verbose_name='Мощность, л.с.')
    type_transmission = models.CharField(max_length=2, choices=TYPE_TRANSMISSION, verbose_name='Коробка передач')
    drive_unit = models.CharField(max_length=10, choices=DRIVE_UNIT, blank=True, null=True, verbose_name='Привод')
    fuel_consumption_mixed = models.IntegerField(blank=True, null=True, verbose_name='Расход топлива смешанный')
    acceleration_to = models.IntegerField(blank=True, null=True, verbose_name='Разгон до 100 км/ч')
    audio_system = models.CharField(max_length=2, choices=AUDIO_SYSTEM, default='1', verbose_name='Аудиосистема')
    subwoofer = models.BooleanField(default=False, blank=True, null=True, verbose_name='Сабвуфер')
    headlights = models.CharField(max_length=15, choices=HEADLIGHTS, default='halogen', verbose_name='Фары')
    fog = models.BooleanField(default=False, verbose_name='Противотуманные ')
    headlight_washers = models.BooleanField(default=False, verbose_name='Омыватели фар')
    adaptive_lighting = models.BooleanField(default=False, verbose_name='Адаптивное освещение')
    tires_and_wheels = models.IntegerField(blank=True, null=True, verbose_name='Шины и диски')
    winter_tires = models.BooleanField(default=False, verbose_name='Зимние шины в комплекте')
    front_seats = models.BooleanField(default=False, verbose_name='Передние сиденья')
    rear_seats = models.BooleanField(default=False, verbose_name='Заднее сиденье')
    mirrors = models.BooleanField(default=False, verbose_name='Зеркал')
    rear_glass = models.BooleanField(default=False, verbose_name='Заднего стекла')
    rudder = models.BooleanField(default=False, verbose_name='Руля')
    body_type = models.ForeignKey(TransportBodyType,
                                  on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип кузова')

    class Meta(
        OperationHistory.Meta, MultimediaAndNavigation.Meta,
        DrivingAssistance.Meta, AntiTheftSystem.Meta,
        Airbags.Meta, ActiveSafety.Meta, AdvertAbstract.Meta,
        CommonTransport.Meta,

    ):
        verbose_name = 'Легковой автомобиль'
        verbose_name_plural = 'Легковые автомобили'

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = self.type_brand.name
        return super().save(*args, **kwargs)


class Motorbike(
    AdvertAbstract, CommonTransport,
    OperationHistory
):
    COLORS = (
            ('white', 'Белый'), ('black', 'Черный'),
            ('gray', 'Серый'), ('brown', 'Коричневый'),
            ('red', 'Красный'), ('green', 'Зеленый'),
            ('blue', 'Синий'), ('pink', 'Розовый'),
            ('violet', 'Фиолетовый')
        )

    TYPE_ENGINE = (
        ('p', 'Бензин'), ('e', 'Электро')
    )

    FUEL_SUPPLY = (
        ('k', 'Карбюратор'), ('i', 'Инжектор')
    )

    TYPE_OF_DRIVE = (
        ('c', 'Цепь'), ('r', 'Ремень'),
        ('k', 'Кордан')
    )

    TYPE_TRANSMISSION = (
        ('a', 'Автоматическая'),
        ('m', 'Механическая'),
        ('v', 'Вариативная'),
        ('r', 'Роботизированная')
    )

    CYLINDER_ARRANGEMENT = (
        ('v', 'V-образное'), ('o', 'Оппозитное'),
        ('r', 'Рядное')
    )

    COOLING = (
        ('v', 'Воздушное'), ('l', 'Жидкосное')
    )

    color = models.CharField(max_length=10, choices=COLORS)
    type_engine = models.CharField(max_length=2, choices=TYPE_ENGINE,
                                   blank=True, null=True, verbose_name='Тип двигателя')
    fuel_supply = models.CharField(max_length=2, choices=FUEL_SUPPLY,
                                   blank=True, null=True , verbose_name='Подача топлива')
    type_of_drive = models.CharField(max_length=2, choices=TYPE_OF_DRIVE,
                                     blank=True, null=True, verbose_name='Тип привода')
    Number_of_cycles = models.SmallIntegerField(verbose_name='Число тактов', help_text='может быть 2 или 4')
    number_of_cylinders = models.SmallIntegerField(verbose_name='Количество цилиндров', help_text='до 1-6')
    type_transmission = models.CharField(max_length=2, choices=TYPE_TRANSMISSION,
                                         blank=True, null=True, verbose_name='Коробка передач')
    cylinder_arrangement = models.CharField(max_length=2, choices=CYLINDER_ARRANGEMENT,
                                            blank=True, null=True)
    cooling = models.CharField(max_length=2, choices=COOLING,
                               blank=True, null=True, verbose_name='Охлаждение')
    electric_starter = models.BooleanField(default=False, verbose_name='электростартер')
    abs = models.BooleanField(default=False, verbose_name='Антиблокировочная система')
    tcs = models.BooleanField(default=False, verbose_name='Трэкшн-контроль')
    start_stop_sys = models.BooleanField(default=False, verbose_name='Система старт-стоп')
    windshield = models.BooleanField(default=False, verbose_name='ветровое стекло')
    cofr = models.BooleanField(default=False, verbose_name='Кофр(мотосумка)')


    class Meta(
        AdvertAbstract.Meta, CommonTransport.Meta,
        OperationHistory.Meta
    ):
        verbose_name = 'Мотоцикл'
        verbose_name_plural = 'Мотоцыклы'

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = self.type_brand.name
        return super().save(*args, **kwargs)


class Bus(
    AdvertAbstract, CommonTransport,  OperationHistory,
):
    body_type = models.ForeignKey(TransportBodyType,
                                  on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Тип кузова')

    class Meta(CommonTransport.Meta, OperationHistory.Meta):
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = self.type_brand.name
        return super().save(*args, **kwargs)


class OtherTransport(AdvertAbstract, CommonTransport):


    class Meta(AdvertAbstract.Meta, CommonTransport.Meta):
        verbose_name = 'Прочий транспорт'
        verbose_name_plural = 'Прочий транспорт'

