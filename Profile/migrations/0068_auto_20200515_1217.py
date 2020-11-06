# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-15 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0067_auto_20200513_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Junior Developer', 'Junior Developer'), ('Vice CEO', 'Vice CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('CEO', 'CEO'), ('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Scrum Master', 'Scrum Master'), ('Intern', 'Intern'), ('Frontend Developer', 'Frontend Developer'), ('Project Manager', 'Project Manager')], default='Junior Developer', max_length=50),
        ),
    ]
