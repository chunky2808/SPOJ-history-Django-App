# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-06 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0002_auto_20180507_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='jain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hits', models.IntegerField()),
            ],
        ),
    ]