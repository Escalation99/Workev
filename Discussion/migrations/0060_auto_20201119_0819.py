# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0059_auto_20200907_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Jobdesc', 'Jobdesc'), ('Other', 'Other'), ('Meeting', 'Meeting'), ('Announcement', 'Announcement')], default='Jobdesc', max_length=50),
        ),
    ]