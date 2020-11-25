# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-19 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0051_auto_20201119_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Alignment Meeting', 'Alignment Meeting'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Code Review', 'Code Review'), ('Sprint Planning', 'Sprint Planning'), ('Regular Meeting', 'Regular Meeting')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Vice CEO', 'Vice CEO'), ('Scrum Master', 'Scrum Master'), ('UI/UX Designer', 'UI/UX Designer'), ('All', 'All'), ('CEO', 'CEO'), ('Intern', 'Intern'), ('Fullstack Developer', 'Fullstack Developer'), ('Junior Developer', 'Junior Developer'), ('Project Manager', 'Project Manager'), ('Backend Developer', 'Backend Developer'), ('Frontend Developer', 'Frontend Developer')], default='All', max_length=50),
        ),
    ]