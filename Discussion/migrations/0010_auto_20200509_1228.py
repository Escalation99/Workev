# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-09 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0009_auto_20200509_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Announcement', 'Announcement'), ('Other', 'Other'), ('Jobdesc', 'Jobdesc'), ('Meeting', 'Meeting')], default='Jobdesc', max_length=50),
        ),
        migrations.AlterField(
            model_name='reply',
            name='title',
            field=models.CharField(blank=True, default='reply', max_length=255),
        ),
    ]