# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-19 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_receipt_is_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='status',
        ),
    ]
