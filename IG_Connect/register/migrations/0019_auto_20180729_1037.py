# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-29 10:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0018_form_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 7, 29, 10, 37, 28, 763124)),
        ),
    ]
