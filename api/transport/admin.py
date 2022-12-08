from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Car, Motorbike, Bus, OtherTransport, TransportBodyType


admin.site.register(Car)
admin.site.register(Motorbike)
admin.site.register(Bus)
admin.site.register(OtherTransport)
admin.site.register(TransportBodyType)