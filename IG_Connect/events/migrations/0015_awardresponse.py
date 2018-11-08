# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-26 21:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0014_event_softreq'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud1', models.CharField(max_length=1000)),
                ('stud2', models.CharField(max_length=1000)),
                ('stud3', models.CharField(max_length=1000)),
                ('stud4', models.CharField(max_length=1000)),
                ('titleofpaper', models.TextField()),
                ('broadfield', models.TextField()),
                ('abstract', models.TextField()),
                ('conclusion', models.TextField()),
                ('googledoc', models.TextField()),
                ('whyaward', models.TextField()),
                ('suggestions', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]