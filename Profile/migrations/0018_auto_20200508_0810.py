# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0017_auto_20200508_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('Junior Developer', 'Junior Developer'), ('Scrum Master', 'Scrum Master'), ('CEO', 'CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Project Manager', 'Project Manager'), ('Vice CEO', 'Vice CEO'), ('Fullstack Developer', 'Fullstack Developer')], default='Junior Developer', max_length=50),
        ),
    ]
