# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0061_auto_20200513_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Junior Developer', 'Junior Developer'), ('Backend Developer', 'Backend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Fullstack Developer', 'Fullstack Developer'), ('CEO', 'CEO'), ('Vice CEO', 'Vice CEO'), ('Frontend Developer', 'Frontend Developer'), ('Intern', 'Intern'), ('Scrum Master', 'Scrum Master'), ('Project Manager', 'Project Manager')], default='Junior Developer', max_length=50),
        ),
    ]
