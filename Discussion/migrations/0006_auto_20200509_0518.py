# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-09 05:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion', '0005_auto_20200509_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Jobdesc', 'Jobdesc'), ('Other', 'Other'), ('Meeting', 'Meeting'), ('Announcement', 'Announcement')], default='Jobdesc', max_length=50),
        ),
        migrations.AlterField(
            model_name='reply',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
