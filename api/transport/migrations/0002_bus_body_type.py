# Generated by Django 4.1.3 on 2022-12-05 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='body_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transport.transportbodytype', verbose_name='Тип кузова'),
        ),
    ]
