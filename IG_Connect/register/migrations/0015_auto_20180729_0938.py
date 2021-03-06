# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-29 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_auto_20180729_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='form',
            name='email',
        ),
        migrations.RemoveField(
            model_name='form',
            name='name',
        ),
        migrations.RemoveField(
            model_name='form',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='form',
            name='year',
        ),
        migrations.AddField(
            model_name='registered',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Form'),
        ),
    ]
