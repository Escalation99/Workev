# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-02 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0062_auto_20201119_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Jobdesc', 'Jobdesc'), ('Other', 'Other'), ('Meeting', 'Meeting'), ('Announcement', 'Announcement')], default='Jobdesc', max_length=50),
        ),
    ]
