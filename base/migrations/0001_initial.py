# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('link', models.TextField(max_length=100, null=True, blank=True, verbose_name='Ссылка на сайт')),
                ('sector', models.CharField(max_length=100, null=True, blank=True, verbose_name='Отрасль')),
                ('phone', models.IntegerField(null=True, blank=True, verbose_name='Телефон')),
                ('address', models.TextField(max_length=200, null=True, blank=True, verbose_name='Адрес')),
                ('vacancy_count', models.IntegerField(default=1, null=True, blank=True, verbose_name='Количество вакансий')),
                ('company_size', models.CharField(max_length=50, null=True, blank=True, verbose_name='Размер компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
    ]
