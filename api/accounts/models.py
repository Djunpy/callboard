from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField
from utils.utils import profile_photo_directory_path
from utils.models import TimeStampedAbstractModel

from address.models import Address

from .managers import CustomUserManager


class User(TimeStampedAbstractModel, AbstractUser):

    email = models.EmailField(max_length=80, unique=True)
    last_visit = models.DateTimeField(blank=True, null=True)
    is_email_verify = models.BooleanField(default=False)


    object = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Profile(TimeStampedAbstractModel):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=profile_photo_directory_path,
                              default='default_photo_profile/noimage.png')
    telegram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        SIZE = 300, 300
        if self.photo:
            pic = Image.open(self.photo.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.photo.path)

    def __str__(self):
        return self.user.email



class PhoneNumber(TimeStampedAbstractModel):
    user = models.OneToOneField(
        User, related_name='phone', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True)
    security_code = models.CharField(max_length=120)
    is_verified = models.BooleanField(default=False)
    sent = models.DateTimeField(null=True)

    class Meta:
        ordering = ('-created', )

