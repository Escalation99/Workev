# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-08 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0079_auto_20200708_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('CEO', 'CEO'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master'), ('UI/UX Designer', 'UI/UX Designer'), ('Fullstack Developer', 'Fullstack Developer'), ('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('Vice CEO', 'Vice CEO'), ('Junior Developer', 'Junior Developer'), ('Intern', 'Intern')], default='Junior Developer', max_length=50),
        ),
    ]
