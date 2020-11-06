# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0012_auto_20200508_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('Vice CEO', 'Vice CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Scrum Master', 'Scrum Master'), ('Project Manager', 'Project Manager'), ('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Intern', 'Intern'), ('Frontend Developer', 'Frontend Developer'), ('Junior Developer', 'Junior Developer'), ('CEO', 'CEO')], default='Junior Developer', max_length=50),
        ),
    ]
