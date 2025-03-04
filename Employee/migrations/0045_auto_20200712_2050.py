# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0044_auto_20200711_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Sprint Retrospective', 'Sprint Retrospective'), ('Sprint Planning', 'Sprint Planning'), ('Regular Meeting', 'Regular Meeting'), ('Code Review', 'Code Review'), ('Alignment Meeting', 'Alignment Meeting')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Vice CEO', 'Vice CEO'), ('Junior Developer', 'Junior Developer'), ('Backend Developer', 'Backend Developer'), ('Project Manager', 'Project Manager'), ('CEO', 'CEO'), ('Scrum Master', 'Scrum Master'), ('Intern', 'Intern'), ('All', 'All'), ('Frontend Developer', 'Frontend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Fullstack Developer', 'Fullstack Developer')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Regular', 'Regular'), ('Online', 'Online')], default='Regular', max_length=255),
        ),
    ]
