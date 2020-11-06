# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0027_auto_20200513_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendance_status',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Alignment Meeting', 'Alignment Meeting'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Regular Meeting', 'Regular Meeting'), ('Sprint Planning', 'Sprint Planning'), ('Code Review', 'Code Review')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('Intern', 'Intern'), ('Backend Developer', 'Backend Developer'), ('Scrum Master', 'Scrum Master'), ('All', 'All'), ('Junior Developer', 'Junior Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Fullstack Developer', 'Fullstack Developer'), ('CEO', 'CEO'), ('Project Manager', 'Project Manager'), ('Vice CEO', 'Vice CEO')], default='All', max_length=50),
        ),
    ]