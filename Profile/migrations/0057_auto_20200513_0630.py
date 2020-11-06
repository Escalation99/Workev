# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0056_auto_20200513_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('CEO', 'CEO'), ('Fullstack Developer', 'Fullstack Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Vice CEO', 'Vice CEO'), ('Junior Developer', 'Junior Developer'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master')], default='Junior Developer', max_length=50),
        ),
    ]