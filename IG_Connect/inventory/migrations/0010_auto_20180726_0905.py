# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-26 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20180713_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrequest',
            name='returnDate',
            field=models.DateField(default=b'2018-07-26'),
        ),
    ]
