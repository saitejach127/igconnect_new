# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-12 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180204_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projecturl',
            field=models.URLField(default=None, max_length=500),
        ),
    ]
