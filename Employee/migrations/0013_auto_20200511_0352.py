# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-11 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0012_auto_20200511_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Sprint Planning', 'Sprint Planning'), ('Regular Meeting', 'Regular Meeting'), ('Alignment Meeting', 'Alignment Meeting'), ('Code Review', 'Code Review'), ('Sprint Retrospective', 'Sprint Retrospective')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('Project Manager', 'Project Manager'), ('UI/UX Designer', 'UI/UX Designer'), ('All', 'All'), ('Fullstack Developer', 'Fullstack Developer'), ('Intern', 'Intern'), ('CEO', 'CEO'), ('Junior Developer', 'Junior Developer'), ('Backend Developer', 'Backend Developer'), ('Scrum Master', 'Scrum Master'), ('Vice CEO', 'Vice CEO')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Online', 'Online'), ('Seminar', 'Seminar'), ('Regular', 'Regular')], default='Regular', max_length=255),
        ),
    ]
