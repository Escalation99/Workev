# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0032_auto_20200513_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Jobdesc', 'Jobdesc'), ('Meeting', 'Meeting'), ('Other', 'Other'), ('Announcement', 'Announcement')], default='Jobdesc', max_length=50),
        ),
    ]
