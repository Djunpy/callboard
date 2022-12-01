from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey

from utils.models import TimeStampedAbstractModel
from utils.utils import advert_picture_directory_path

User = get_user_model()


class AdvertCategory(MPTTModel):

    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class AutoBrand(MPTTModel):

    name = models.CharField(max_length=80, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Picture(models.Model):

    img = models.ImageField(upload_to=advert_picture_directory_path)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинка'


class Discount(TimeStampedAbstractModel):

    sum = models.DecimalField(max_digits=10, decimal_places=2)
    ends = models.DateTimeField(blank=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.sum


class CommonAdvertAbstract(models.Model):

    CONDITION = (
        ('b', 'Плохое'),
        ('m', 'Среднее'),
        ('g', 'Хорошее')
    )

    price = models.DecimalField(max_digits=10, decimal_places=2,
                                blank=True, null=True)
    discount = models.ManyToManyField(Discount)
    condition = models.CharField(max_length=5, choices=CONDITION, default='g')

    class Meta:
        abstract = True


class AdvertAbstract(models.Model):

    TYPE_OF_CMMUNICATION = (
        ('call', 'Позвонить'),
        ('write', 'Написать'),
        ('all', 'Любой из указанных')
    )

    STATUS = (
        ('published', 'Опубликована'),
        ('draft', 'В черновике'),
        ('ban', 'В бане')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='advert')
    bookmarks = models.ManyToManyField(User, related_name='bookmarks',
                                       blank=True)
    contact = models.CharField(max_length=10, choices=TYPE_OF_CMMUNICATION,
                               default='all')
    pictures = models.ManyToManyField(Picture)
    category = models.ForeignKey(AdvertCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    address = models.ForeignKey('address.Address', on_delete=models.SET_NULL,
                                blank=True, null=True)

    views = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Auto(AdvertAbstract, CommonAdvertAbstract):

    TYPE_TRANSMISSION = (
        ('a', 'Автоматическая'),
        ('m', 'Механическая'),
        ('v', 'Вариативная'),
        ('r', 'Роботизированная')
    )

    TYPE_ENGINE = (
        ('p', 'Бензин'), ('g', 'Газ'),
        ('d', 'Дизель'), ('gb', 'гибридные'),
        ('e', 'Электро')
    )

    COLORS = (
        ('white', 'Белый'), ('black', 'Черный'),
        ('gray', 'Серый'), ('brown', 'Коричневый'),
        ('red', 'Красный'), ('green', 'Зеленый'),
        ('blue', 'Синий'), ('pink', 'Розовый')
    )

    BODY_TYPE = (
        ('se', 'Седан'), ('un', 'Универсал'),
        ('ha', 'Хэтчбек'), ('lb', 'Лифтбек'),
        ('cp', 'Купе'), ('lm', 'Лимузин'),
        ('suv', 'Внедорожник'), ('pic', 'Пикап'),
        ('mn', 'Минивен'), ('fr', 'Фургон'),
        ('mcra', 'Микроавтобус')
    )

    DRIVE_UNIT = (
        ('front', 'Передний'), ('real', 'Задний'),
        ('full', 'Полный'), ('hybrid', 'Гибридный')
    )

    brand = models.ForeignKey(AutoBrand, on_delete=models.CASCADE)
    release = models.DateField(blank=True, null=True)
    transmission = models.CharField(max_length=5, choices=TYPE_TRANSMISSION,
                                    default='m')
    number_owner = models.IntegerField(blank=True, null=transmission)
    color = models.CharField(max_length=15, choices=COLORS,
                             blank=True, null=True)
    body_type = models.CharField(max_length=10, choices=BODY_TYPE)
    engine_volume = models.CharField(max_length=10, blank=True, null=True)
    engine_type = models.CharField(max_length=5, choices=TYPE_ENGINE, default='p')
    drive_unit = models.CharField(max_length=10, choices=DRIVE_UNIT, blank=True, null=True)
    mileage = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.name


class Property(AdvertAbstract, CommonAdvertAbstract):

    TYPE_PROPERTY = (
        ('flat', 'Квартира'), ('room', 'Комната'),
        ('hous', 'Дом'), ('lploat', 'Земельный участок'),
        ('garage', 'Гараж, и машино место')
    )

    TYPE_OFFER = (
        ('sell', 'Продать'), ('handov', 'Сдать')
    )
    type_property = models.CharField(max_length=20, choices=TYPE_PROPERTY,
                                     default='flat')
    type_offer = models.CharField(max_length=20, choices=TYPE_OFFER, default='sell')
    rooms = models.IntegerField(default=1)
    studio = models.BooleanField(default=False)
    balcony = models.CharField(max_length=120, blank=True, null=True)
    technique = models.CharField(max_length=250, blank=True, null=True)
    foor = models.CharField(max_length=80, blank=True, null=True)
    square = models.CharField(max_length=80, blank=True, null=True)
    Internet = models.CharField(max_length=80, blank=True, null=True)
    parking = models.CharField(max_length=80, blank=True, null=True)
    children_allowed = models.BooleanField(default=True)
    smoke_allowed = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)
    party_allowed = models.BooleanField(default=False)
    contract_price = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'


# class JobArea(MPTTModel):
#     name = models.CharField(max_length=50, unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE,
#                             null=True, blank=True, related_name='children')
#
#     class MPTTMeta:
#         order_insertion_by = ['name']


class Vacancy(AdvertAbstract, CommonAdvertAbstract):

    SHEDULE = (
        ('full', 'Полный день'), ('partial', 'Не полный'),
        ('remote', 'Удаленный'), ('freesdule', 'Свободный график'),
        ('Shwork', 'Сменный график'), ('shishdule', 'Вахтовый')

    )

    TYPE_PAYOUT = (
        ('hpayment', 'Почасовая оплата'),
        ('dpayment', 'Каждый день'),
        ('onemonth', 'Один раз в месяц'),
        ('twomonth', 'Два раза в месяц')
    )

    schedule = models.CharField(max_length=20, choices=SHEDULE, default='full')
    work_experience = models.IntegerField(default=0)
    without_experience = models.BooleanField(default=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    type_payout = models.CharField(max_length=20, choices=TYPE_PAYOUT,
                                   default='onemonth')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class ServiceType(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class Service(AdvertAbstract, CommonAdvertAbstract):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'