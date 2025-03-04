# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0038_auto_20200510_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Scrum Master', 'Scrum Master'), ('Fullstack Developer', 'Fullstack Developer'), ('Backend Developer', 'Backend Developer'), ('CEO', 'CEO'), ('Intern', 'Intern'), ('UI/UX Designer', 'UI/UX Designer'), ('Project Manager', 'Project Manager'), ('Junior Developer', 'Junior Developer'), ('Vice CEO', 'Vice CEO'), ('Frontend Developer', 'Frontend Developer')], default='Junior Developer', max_length=50),
        ),
    ]
