# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-11 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0016_auto_20200511_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='new', max_length=20),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Sprint Retrospective', 'Sprint Retrospective'), ('Code Review', 'Code Review'), ('Alignment Meeting', 'Alignment Meeting'), ('Sprint Planning', 'Sprint Planning'), ('Regular Meeting', 'Regular Meeting')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Scrum Master', 'Scrum Master'), ('Frontend Developer', 'Frontend Developer'), ('Intern', 'Intern'), ('CEO', 'CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Fullstack Developer', 'Fullstack Developer'), ('Vice CEO', 'Vice CEO'), ('Backend Developer', 'Backend Developer'), ('Junior Developer', 'Junior Developer'), ('Project Manager', 'Project Manager'), ('All', 'All')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Regular', 'Regular'), ('Online', 'Online')], default='Regular', max_length=255),
        ),
    ]
