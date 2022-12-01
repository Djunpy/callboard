from django.db import models
from django.contrib.auth import get_user_model

from utils.models import TimeStampedAbstractModel


User = get_user_model()


class Complaint(TimeStampedAbstractModel):
    TYPES_COMPLAINT = (
        ('1', 'Мошенничество'),
        ('2', 'Продажа заприщенных товаров'),
        ('3', 'Оскорбление'),
        ('4', 'Другое')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='complaint')
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='complaint_by')
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'
        ordering = ('-created',)

    def __str__(self):
        return self.user.username