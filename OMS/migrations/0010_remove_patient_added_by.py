# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OMS', '0009_auto_20170301_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='added_by',
        ),
    ]
