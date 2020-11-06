# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0038_auto_20200513_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Other', 'Other'), ('Meeting', 'Meeting'), ('Announcement', 'Announcement'), ('Jobdesc', 'Jobdesc')], default='Jobdesc', max_length=50),
        ),
    ]