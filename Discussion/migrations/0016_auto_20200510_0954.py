# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0015_auto_20200510_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Announcement', 'Announcement'), ('Meeting', 'Meeting'), ('Other', 'Other'), ('Jobdesc', 'Jobdesc')], default='Jobdesc', max_length=50),
        ),
    ]
