# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0054_auto_20200711_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Jobdesc', 'Jobdesc'), ('Other', 'Other'), ('Meeting', 'Meeting'), ('Announcement', 'Announcement')], default='Jobdesc', max_length=50),
        ),
    ]
