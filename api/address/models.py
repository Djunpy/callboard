from django.db import models

from utils.models import TimeStampedAbstractModel


class Country(models.Model):
    name = models.CharField(max_length=80, unique=True)

class City(models.Model):
    name = models.CharField(max_length=80, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
class Address(TimeStampedAbstractModel):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=5, blank=True, null=True)
    apartment_number = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'Country:{self.country}, City: {self.city}'




