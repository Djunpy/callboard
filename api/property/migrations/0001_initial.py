# Generated by Django 4.1.3 on 2022-12-08 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('advert', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(choices=[('call', 'Позвонить'), ('write', 'Написать'), ('all', 'Любой из указанных')], default='all', max_length=10)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('published', 'Опубликована'), ('draft', 'В черновике'), ('ban', 'В бане')], default='draft', max_length=20)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('type_plot', models.CharField(choices=[('agriculture', 'Под сельское хозяйство'), ('construction', 'Под строительство')], default='agriculture', max_length=15, verbose_name='Тип участка')),
                ('land_area', models.FloatField(verbose_name='Площадь земли')),
                ('gas', models.BooleanField(default=False, verbose_name='Газофикация')),
                ('water_supply', models.BooleanField(default=False, verbose_name='Водоснабжение')),
                ('sewerage', models.BooleanField(default=False, verbose_name='Канализация')),
                ('power_supply', models.BooleanField(default=False, verbose_name='Электроснабжение')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address')),
                ('bookmarks', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_bookmarks', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.advertcategory')),
                ('pictures', models.ManyToManyField(to='advert.picture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_adverts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участки',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(choices=[('call', 'Позвонить'), ('write', 'Написать'), ('all', 'Любой из указанных')], default='all', max_length=10)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('published', 'Опубликована'), ('draft', 'В черновике'), ('ban', 'В бане')], default='draft', max_length=20)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('repair', models.CharField(choices=[('required', 'Требуется'), ('cosmetic', 'Косметический'), ('euro', 'Евро'), ('disigner', 'Дизайнерский')], default='design', max_length=15, verbose_name='Ремонт')),
                ('floor_in_house', models.SmallIntegerField(verbose_name='Этажей в доме')),
                ('tv', models.BooleanField(default=False, verbose_name='Телевидение')),
                ('internet', models.BooleanField(default=False, verbose_name='Интернет')),
                ('parking', models.CharField(choices=[('no', 'Нет'), ('garage', 'Гараж'), ('parkingspace', 'Парковочное место')], default='no', max_length=15)),
                ('type_house', models.CharField(choices=[('house', 'Дом'), ('dacha', 'Дача'), ('cottage', 'Котедж'), ('townhouse', 'Таунхаус')], default='dacha', max_length=15, verbose_name='Вид объекта')),
                ('wall_material', models.CharField(choices=[('brick', 'Кирпич'), ('timber', 'Брус'), ('log', 'Брус'), ('metal', 'Металл'), ('gasblock', 'Газоблоки'), ('penoblock', 'Пеноблоки')], default='brick', max_length=15, verbose_name='Материал стен')),
                ('bath', models.BooleanField(default=False, verbose_name='Баня')),
                ('poll', models.BooleanField(default=False, verbose_name='бассейн')),
                ('year_of_construction', models.SmallIntegerField(verbose_name='Год постройкпи')),
                ('number_of_rooms', models.SmallIntegerField(verbose_name='Количество комнат')),
                ('house_area', models.FloatField(verbose_name='Площадь дома')),
                ('land_area', models.FloatField(verbose_name='Площадь участка')),
                ('bathroom_street', models.BooleanField(default=False, verbose_name='Санузел на улице')),
                ('bathroom_house', models.BooleanField(default=False, verbose_name='Санузел в доме')),
                ('asphalt_road', models.BooleanField(default=False, verbose_name='Асфальтированная дорога')),
                ('public_transport', models.BooleanField(default=False, verbose_name='Остановка общественного транспорта ')),
                ('pharmacy', models.BooleanField(default=False, verbose_name='Аптека')),
                ('shop', models.BooleanField(default=False, verbose_name='Магазин')),
                ('kindergarten', models.BooleanField(default=False, verbose_name='Детский сад')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address')),
                ('bookmarks', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_bookmarks', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.advertcategory')),
                ('pictures', models.ManyToManyField(to='advert.picture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_adverts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Дома и дачи',
                'verbose_name_plural': 'Дома и дачи',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(choices=[('call', 'Позвонить'), ('write', 'Написать'), ('all', 'Любой из указанных')], default='all', max_length=10)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('published', 'Опубликована'), ('draft', 'В черновике'), ('ban', 'В бане')], default='draft', max_length=20)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('repair', models.CharField(choices=[('required', 'Требуется'), ('cosmetic', 'Косметический'), ('euro', 'Евро'), ('disigner', 'Дизайнерский')], default='design', max_length=15, verbose_name='Ремонт')),
                ('floor_in_house', models.SmallIntegerField(verbose_name='Этажей в доме')),
                ('tv', models.BooleanField(default=False, verbose_name='Телевидение')),
                ('internet', models.BooleanField(default=False, verbose_name='Интернет')),
                ('floor', models.SmallIntegerField(verbose_name='Этаж')),
                ('house_type', models.CharField(choices=[('brick', 'Кирпичный'), ('panel', 'Панельный'), ('blocky', 'Блочный'), ('monolit', 'Монолитный'), ('monolit-brick', 'Монолитно-Кирпичный'), ('wood', 'Деревянный')], default='brick', max_length=20, verbose_name='Тип дома')),
                ('parking', models.CharField(choices=[('under', 'Подземная'), ('yarn', 'Открытая во дворе'), ('garage', 'Гараж')], default='yard', max_length=15)),
                ('housing_stock', models.CharField(choices=[('primary', 'Первичка'), ('resale', 'Вторичка')], default='primary', max_length=10, verbose_name='Жилой фонд')),
                ('balcony', models.BooleanField(default=False, verbose_name='Балкон')),
                ('loggia', models.BooleanField(default=False, verbose_name='Лоджия')),
                ('bathroom', models.CharField(choices=[('combined', 'Совмещенный'), ('divided', 'Разделенный')], default='divided', max_length=10, verbose_name='Тип санузла')),
                ('furniture_kitchen', models.BooleanField(default=False, verbose_name='Кухонная мебель')),
                ('furniture_clothes_places', models.BooleanField(default=False, verbose_name='Мебель для хранения одежды')),
                ('furniture_sleeping_places', models.BooleanField(default=False, verbose_name='Спальные места')),
                ('washing_machine', models.BooleanField(default=False, verbose_name='Стиральная машина')),
                ('dishwasher', models.BooleanField(default=False, verbose_name='Посудомоечная машина')),
                ('total_area', models.FloatField(verbose_name='Общая площадь')),
                ('living_space', models.FloatField(verbose_name='Жилая площадь')),
                ('number_of_rooms', models.SmallIntegerField(verbose_name='Количество комнат')),
                ('ceiling_height', models.FloatField(verbose_name='Высота потолков')),
                ('type_offer', models.CharField(choices=[('sell', 'Продать'), ('pass', 'Сдать')], default='sell', max_length=10, verbose_name='Тип предложения')),
                ('conditioner', models.BooleanField(default=False, verbose_name='Кондиционер')),
                ('fridge', models.BooleanField(default=False, verbose_name='Холодильник')),
                ('elevator', models.BooleanField(default=False, verbose_name='Лифт')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address')),
                ('bookmarks', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_bookmarks', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.advertcategory')),
                ('pictures', models.ManyToManyField(to='advert.picture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_adverts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Квартиры и комнаты',
                'verbose_name_plural': 'Квартиры и комнаты',
                'abstract': False,
            },
        ),
    ]
