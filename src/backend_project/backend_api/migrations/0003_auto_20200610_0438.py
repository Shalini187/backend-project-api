# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-10 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_auto_20200605_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='user_location',
            field=models.CharField(choices=[('Europe/London', 'Europe/London'), ('Asia/Kolkata', 'Asia/Kolkata'), ('America/Los_Angeles', 'America/Los_Angeles'), ('Asia/Shanghai', 'Asia/Shanghai'), ('Africa/Brazzaville', 'Africa/Brazzaville'), ('Australia/Lindeman', 'Australia/Lindeman'), ('Chile/Continental', 'Chile/Continental'), ('Mexico/BajaSur', 'Africa/Brazzaville')], max_length=256, verbose_name='user location'),
        ),
    ]
