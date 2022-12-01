from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Profile
from complaint.models import Complaint

User = get_user_model()


class ComplaintAdminInline(admin.StackedInline):
    model = Complaint


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_image', 'get_address')
    list_filter = ('user', 'created')
    search_fields = ('user',)


    def get_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src={obj.photo.url} width="100" height="110"')

    def get_address(self, obj):
        if hasattr(obj, 'country'):
            return f'Coutry: {obj.address.country}'
        return '---'


class UserProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    inlines = [UserProfileInline]
    model = User

    list_display = ('username', 'email', 'is_email_verify', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('is_active', 'is_email_verify', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('created',)

    def get_complaint(self, obj):
        if hasattr(obj, 'complaint_set'):
            return obj.complaint_set


