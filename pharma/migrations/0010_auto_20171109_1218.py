# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pharma', '0009_auto_20171109_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='c_id',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealer',
            name='c_id',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='e_id',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='p_id',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]