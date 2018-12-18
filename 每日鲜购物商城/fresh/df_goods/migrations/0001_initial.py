# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gtitle', models.CharField(max_length=20, unique=True)),
                ('gpic', models.ImageField(upload_to='images/goods')),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gunit', models.CharField(max_length=20, default='500g')),
                ('gclick', models.IntegerField(default=0)),
                ('gintroduction', models.CharField(max_length=200)),
                ('gstock', models.IntegerField(default=0)),
                ('gcontect', tinymce.models.HTMLField()),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ttitle', models.CharField(max_length=20, unique=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtypeinfo',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
