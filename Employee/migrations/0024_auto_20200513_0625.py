# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0023_auto_20200513_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='clock_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Sprint Retrospective', 'Sprint Retrospective'), ('Code Review', 'Code Review'), ('Regular Meeting', 'Regular Meeting'), ('Alignment Meeting', 'Alignment Meeting'), ('Sprint Planning', 'Sprint Planning')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Intern', 'Intern'), ('UI/UX Designer', 'UI/UX Designer'), ('All', 'All'), ('CEO', 'CEO'), ('Backend Developer', 'Backend Developer'), ('Project Manager', 'Project Manager'), ('Vice CEO', 'Vice CEO'), ('Scrum Master', 'Scrum Master'), ('Junior Developer', 'Junior Developer'), ('Frontend Developer', 'Frontend Developer'), ('Fullstack Developer', 'Fullstack Developer')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Online', 'Online'), ('Seminar', 'Seminar')], default='Regular', max_length=255),
        ),
    ]