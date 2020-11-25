# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0052_auto_20201119_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Alignment Meeting', 'Alignment Meeting'), ('Regular Meeting', 'Regular Meeting'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Code Review', 'Code Review'), ('Sprint Planning', 'Sprint Planning')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('All', 'All'), ('Fullstack Developer', 'Fullstack Developer'), ('CEO', 'CEO'), ('Backend Developer', 'Backend Developer'), ('Frontend Developer', 'Frontend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master'), ('Junior Developer', 'Junior Developer'), ('Intern', 'Intern'), ('Vice CEO', 'Vice CEO')], default='All', max_length=50),
        ),
    ]
