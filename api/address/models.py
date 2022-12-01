from django.db import models

from utils.models import TimeStampedAbstractModel


class Address(TimeStampedAbstractModel):

    CHOICE_COUNTRY = (
        ('md', 'Молдова'),
        ('pmr', 'Приднестровье'),
    )

    country = models.CharField(max_length=5, choices=CHOICE_COUNTRY)
    city = models.CharField(max_length=80)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=5, blank=True, null=True)
    apartment_number = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'Country:{self.country}, City: {self.city}'




