# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-29 08:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
