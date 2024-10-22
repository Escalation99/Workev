# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-11 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0048_auto_20200511_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('Fullstack Developer', 'Fullstack Developer'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Junior Developer', 'Junior Developer'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master')], default='Junior Developer', max_length=50),
        ),
    ]
