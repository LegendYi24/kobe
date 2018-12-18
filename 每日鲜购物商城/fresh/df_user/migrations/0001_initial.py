# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=50, default='d538aff65dc411e8b5b210c37be96a5a', serialize=False)),
                ('uname', models.CharField(max_length=20, unique=True)),
                ('user', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemail', models.EmailField(max_length=254)),
                ('ureceive', models.CharField(max_length=100, default='')),
                ('uaddress', models.CharField(max_length=100, default='')),
                ('uzipcode', models.CharField(max_length=6, default='')),
                ('uphone', models.CharField(max_length=11, default='')),
            ],
        ),
    ]
