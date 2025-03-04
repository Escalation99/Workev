# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_auto_20200510_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Alignment Meeting', 'Alignment Meeting'), ('Regular Meeting', 'Regular Meeting'), ('Sprint Planning', 'Sprint Planning'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Code Review', 'Code Review')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Online', 'Online'), ('Seminar', 'Seminar')], default='Regular', max_length=255),
        ),
    ]
