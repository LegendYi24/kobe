# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('count', models.IntegerField()),
                ('isdelete', models.BooleanField(default=False)),
                ('goodsinfo', models.ForeignKey(to='df_goods.GoodsInfo')),
                ('userinfo', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
    ]
