from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey

from utils.models import TimeStampedAbstractModel
from utils.utils import advert_picture_directory_path

User = get_user_model()


class AdvertSearchManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = Q(name__icontains=query)
            qs = qs.filter(or_lookup).distinct() # Исключаем дубликаты
        return qs

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


class Brand(MPTTModel):

    name = models.CharField(max_length=80, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Бранд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Picture(models.Model):

    img = models.ImageField(upload_to=advert_picture_directory_path,
                            default='default_photo_profile/noimage.png')

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


class CommonConditionChoice(models.Model):
    CONDITION = (
        ('new', 'Новое'), ('bu', 'Б/У')
    )

    condition = models.CharField(max_length=5, choices=CONDITION, default='new')

    class Meta:
        abstract = True


class CommonAdvertAbstract(models.Model):

    price = models.DecimalField(max_digits=10, decimal_places=2,
                                blank=True, null=True)
    discount = models.ManyToManyField(Discount)

    class Meta:
        abstract = True


class Condition(models.Model):
    condition = models.CharField(max_length=30, blank=True, null=True, verbose_name='Состояние')

    class Meta:
        verbose_name = 'Состояние обьявления'
        verbose_name_plural = 'Состояния обьявления'

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

    condition = models.ForeignKey(Condition, on_delete=models.SET_NULL, blank=True, null=True, verbose_name= 'Состояние обьявления')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="%(app_label)s_%(class)s_adverts")
    bookmarks = models.ManyToManyField(User, blank=True, related_name="%(app_label)s_%(class)s_bookmarks")
    contact = models.CharField(max_length=10, choices=TYPE_OF_CMMUNICATION,
                               default='all')
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pictures = models.ManyToManyField(Picture)
    category = models.ForeignKey(AdvertCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    address = models.ForeignKey('address.Address', on_delete=models.SET_NULL,
                                blank=True, null=True)
    views = models.IntegerField(default=0)

    objects = models.Manager()
    search_object = AdvertSearchManager()
    class Meta:
        abstract = True


