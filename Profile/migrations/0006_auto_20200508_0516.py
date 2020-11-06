# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0005_auto_20200508_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='undefined', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='undefined', max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('Project Manager', 'Project Manager'), ('Junior Developer', 'Junior Developer'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO'), ('Intern', 'Intern'), ('UI/UX Designer', 'UI/UX Designer'), ('Frontend Developer', 'Frontend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Scrum Master', 'Scrum Master'), ('Backend Developer', 'Backend Developer')], default='Junior Developer', max_length=50),
        ),
    ]