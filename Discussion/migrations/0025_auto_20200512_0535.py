# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-12 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0024_auto_20200511_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Other', 'Other'), ('Jobdesc', 'Jobdesc'), ('Announcement', 'Announcement'), ('Meeting', 'Meeting')], default='Jobdesc', max_length=50),
        ),
    ]
