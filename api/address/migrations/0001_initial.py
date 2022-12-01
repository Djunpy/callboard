# Generated by Django 4.1.3 on 2022-11-29 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(choices=[('md', 'Молдова'), ('pmr', 'Приднестровье')], max_length=5)),
                ('city', models.CharField(max_length=80)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('house_number', models.CharField(blank=True, max_length=5, null=True)),
                ('apartment_number', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]
