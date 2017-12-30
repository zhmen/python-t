# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 06:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_user_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='delivery_address',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_seller',
            field=models.BooleanField(default=False, help_text='Отметьте, чтобы пользователь мог взаимодействовать только со своими клиентами.', verbose_name='менеджер по продажам'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.DecimalField(decimal_places=0, error_messages={'min_value': 'Номер телефона указывается без восьмёрки, должен содержать 10 цифр и не должен начинаться с 0', 'unique': 'Пользователь с таким номера телефона уже существует'}, max_digits=10, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)], verbose_name='номер телефона'),
        ),
    ]