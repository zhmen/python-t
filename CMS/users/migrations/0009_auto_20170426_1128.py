# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_wholesale_buyer_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='allow_call',
        ),
        migrations.RemoveField(
            model_name='user',
            name='allow_email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='allow_sms',
        ),
    ]