# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-12 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=255)),
                ('contributors', models.CharField(max_length=500)),
                ('exp', models.TextField(max_length=50000)),
            ],
        ),
    ]
