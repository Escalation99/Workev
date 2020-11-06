# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-12 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0049_auto_20200511_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('Junior Developer', 'Junior Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Scrum Master', 'Scrum Master'), ('CEO', 'CEO'), ('Vice CEO', 'Vice CEO'), ('Intern', 'Intern'), ('Project Manager', 'Project Manager'), ('Backend Developer', 'Backend Developer'), ('UI/UX Designer', 'UI/UX Designer')], default='Junior Developer', max_length=50),
        ),
    ]
