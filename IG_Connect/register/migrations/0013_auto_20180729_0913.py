# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-29 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20180729_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
