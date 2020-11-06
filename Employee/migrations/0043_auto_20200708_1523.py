# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-08 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0042_auto_20200708_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Deadline (mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Sprint Planning', 'Sprint Planning'), ('Regular Meeting', 'Regular Meeting'), ('Code Review', 'Code Review'), ('Alignment Meeting', 'Alignment Meeting'), ('Sprint Retrospective', 'Sprint Retrospective')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('CEO', 'CEO'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master'), ('UI/UX Designer', 'UI/UX Designer'), ('All', 'All'), ('Fullstack Developer', 'Fullstack Developer'), ('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('Vice CEO', 'Vice CEO'), ('Junior Developer', 'Junior Developer'), ('Intern', 'Intern')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Regular', 'Regular'), ('Online', 'Online')], default='Regular', max_length=255),
        ),
    ]