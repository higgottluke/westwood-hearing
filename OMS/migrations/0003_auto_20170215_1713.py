# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 01:13
from __future__ import unicode_literals

import OMS.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMS', '0002_audiogram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Visit Date')),
                ('appttype', models.CharField(choices=[('N', 'New Patient - Scheduled'), ('W', 'New Patient - Walk In'), ('C', 'Check-Up'), ('R', 'Reprogram, Refit, or Repair'), ('S', 'Existing Patient - New Sale')], default='', max_length=1, verbose_name='Appointment Type')),
                ('notes', models.TextField(verbose_name='Description and Notes')),
            ],
        ),
        migrations.AddField(
            model_name='audiogram',
            name='notes',
            field=models.TextField(default='', verbose_name='Notes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.TextField(default='', verbose_name='Notes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L1000',
            field=models.SmallIntegerField(default='0', verbose_name='Left 1000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L1500',
            field=models.SmallIntegerField(default='0', verbose_name='Left 1500'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L2000',
            field=models.SmallIntegerField(default='0', verbose_name='Left 2000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L250',
            field=models.SmallIntegerField(default='0', verbose_name='Left 250'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L3000',
            field=models.SmallIntegerField(default='0', verbose_name='Left 3000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L4000',
            field=models.SmallIntegerField(default='0', verbose_name='Left 4000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L500',
            field=models.SmallIntegerField(default='0', verbose_name='Left 500'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L6000',
            field=models.SmallIntegerField(default='0', verbose_name='Left 6000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='L8000',
            field=models.SmallIntegerField(default='0', verbose_name='Left 8000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R1000',
            field=models.SmallIntegerField(default='0', verbose_name='Right 1000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R1500',
            field=models.SmallIntegerField(default='0', verbose_name='Right 1500'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R2000',
            field=models.SmallIntegerField(default='0', verbose_name='Right 2000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R250',
            field=models.SmallIntegerField(default='0', verbose_name='Right 250'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R3000',
            field=models.SmallIntegerField(default='0', verbose_name='Right 3000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R4000',
            field=models.SmallIntegerField(default='0', verbose_name='Right 4000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R500',
            field=models.SmallIntegerField(default='0', verbose_name='Right 500'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R6000',
            field=models.SmallIntegerField(default='0', verbose_name='Right 6000'),
        ),
        migrations.AlterField(
            model_name='audiogram',
            name='R8000',
            field=models.SmallIntegerField(default='0', verbose_name='Right 8000'),
        ),
        migrations.AlterField(
            model_name='owneddevice',
            name='deliverdate',
            field=models.DateTimeField(verbose_name='Delivered on'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=OMS.models.Patient, to='OMS.Patient'),
        ),
    ]
