# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-08 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0052_auto_20200708_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Other', 'Other'), ('Announcement', 'Announcement'), ('Meeting', 'Meeting'), ('Jobdesc', 'Jobdesc')], default='Jobdesc', max_length=50),
        ),
    ]