# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-02 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20181102_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='pat_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
