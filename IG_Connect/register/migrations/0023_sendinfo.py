# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-08 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0022_auto_20180804_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ctc', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]