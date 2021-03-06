# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('OMS', '0003_auto_20170215_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birthday',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Birthday'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Purchased on'),
            preserve_default=False,
        ),
    ]
