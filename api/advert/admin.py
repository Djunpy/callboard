from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin


from .models import AdvertCategory


class AdvertCategoryMPTTAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


# @admin.register(Advert)
# class AdvertAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_discount', 'published', 'status', 'views')
#     list_filter = ('status', 'views', 'published')
#     search_fields = ('title', 'user')
#     list_editable = ('status',)
#
#     def get_image(self, obj):
#         if obj.image:
#             return mark_safe(f'<img src={obj.pictures[0].url} width="100" height="110"')
#
#     def get_discount(self, obj):
#         if hasattr(obj, 'discount'):
#             return obj.discount.sum


admin.site.register(AdvertCategory, AdvertCategoryMPTTAdmin)