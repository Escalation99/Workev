# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-15 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0071_auto_20200516_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Scrum Master', 'Scrum Master'), ('Intern', 'Intern'), ('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Frontend Developer', 'Frontend Developer'), ('Project Manager', 'Project Manager'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Junior Developer', 'Junior Developer')], default='Junior Developer', max_length=50),
        ),
    ]
