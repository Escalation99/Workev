# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0010_auto_20200509_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Meeting', 'Meeting'), ('Jobdesc', 'Jobdesc'), ('Announcement', 'Announcement'), ('Other', 'Other')], default='Jobdesc', max_length=50),
        ),
    ]
