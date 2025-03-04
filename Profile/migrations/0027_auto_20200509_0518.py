# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-09 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0026_auto_20200509_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Fullstack Developer', 'Fullstack Developer'), ('Backend Developer', 'Backend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('CEO', 'CEO'), ('Project Manager', 'Project Manager'), ('Vice CEO', 'Vice CEO'), ('Intern', 'Intern'), ('Scrum Master', 'Scrum Master'), ('Junior Developer', 'Junior Developer'), ('Frontend Developer', 'Frontend Developer')], default='Junior Developer', max_length=50),
        ),
    ]
