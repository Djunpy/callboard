from django.contrib import admin

from .models import Address, City, Country


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city')
    list_filter = ('country',)

admin.site.register(Country)
admin.site.register(City)