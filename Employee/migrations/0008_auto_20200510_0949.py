# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_auto_20200510_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Alignment Meeting', 'Alignment Meeting'), ('Sprint Planning', 'Sprint Planning'), ('Regular Meeting', 'Regular Meeting'), ('Code Review', 'Code Review'), ('Sprint Retrospective', 'Sprint Retrospective')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Online', 'Online'), ('Seminar', 'Seminar'), ('Regular', 'Regular')], default='Regular', max_length=255),
        ),
    ]
