# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-15 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0068_auto_20200515_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Project Manager', 'Project Manager'), ('Frontend Developer', 'Frontend Developer'), ('Vice CEO', 'Vice CEO'), ('Scrum Master', 'Scrum Master'), ('Backend Developer', 'Backend Developer'), ('CEO', 'CEO'), ('Fullstack Developer', 'Fullstack Developer'), ('Intern', 'Intern'), ('UI/UX Designer', 'UI/UX Designer'), ('Junior Developer', 'Junior Developer')], default='Junior Developer', max_length=50),
        ),
    ]
