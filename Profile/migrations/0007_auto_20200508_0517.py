# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_auto_20200508_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('Scrum Master', 'Scrum Master'), ('Intern', 'Intern'), ('CEO', 'CEO'), ('Vice CEO', 'Vice CEO'), ('Backend Developer', 'Backend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Frontend Developer', 'Frontend Developer'), ('Junior Developer', 'Junior Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Project Manager', 'Project Manager')], default='Junior Developer', max_length=50),
        ),
    ]
