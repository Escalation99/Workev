# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-11 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0053_auto_20200708_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Announcement', 'Announcement'), ('Jobdesc', 'Jobdesc'), ('Other', 'Other'), ('Meeting', 'Meeting')], default='Jobdesc', max_length=50),
        ),
    ]