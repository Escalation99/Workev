# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0061_auto_20201119_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Announcement', 'Announcement'), ('Other', 'Other'), ('Meeting', 'Meeting'), ('Jobdesc', 'Jobdesc')], default='Jobdesc', max_length=50),
        ),
    ]
