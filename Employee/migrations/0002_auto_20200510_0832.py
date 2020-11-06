# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='location',
            new_name='room',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Regular Meeting', 'Regular Meeting'), ('Code Review', 'Code Review'), ('Sprint Planning', 'Sprint Planning'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Alignment Meeting', 'Alignment Meeting')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Regular Meeting', 'Regular Meeting'), ('Webex Meeting', 'Webex Meeting'), ('Zoom Meeting', 'Zoom Meeting')], default='Regular Meeting', max_length=255),
        ),
    ]