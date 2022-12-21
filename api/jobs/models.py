from django.db import models

from advert.models import AdvertAbstract


class Profession(models.Model):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Job(AdvertAbstract):

    SCHEDULE = (
        ('full', 'Полный рабочий день'), ('notfull', 'Не полный рабочий день'),
        ('free', 'Свободный график'), ('shiftwork', 'Сменный график'),
        ('remote', 'Удаленная работа'), ('shiftshedule', 'Вахтовый метод')
    )

    PAYOUT = (
        ('hpayment', 'Почасовая оплата'), ('hpayment', 'Каждый день'),
        ('onemonth', 'Раз в месяц'), ('twomounth', 'Дважды в месяц')
    )



    payout = models.CharField(max_length=15, choices=PAYOUT, default='hpayment', verbose_name='Частота выплат')
    schedule = models.CharField(max_length=15, choices=SCHEDULE, default='full')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name='Профессия')
    from_salary = models.DecimalField(verbose_name='От определенной суммы')
    before_salary = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True, verbose_name='До определенной суммы')
    without_experience = models.BooleanField(default=False)
    work_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'