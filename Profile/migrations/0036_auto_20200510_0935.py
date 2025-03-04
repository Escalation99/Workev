# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0035_auto_20200510_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Fullstack Developer', 'Fullstack Developer'), ('Junior Developer', 'Junior Developer'), ('Intern', 'Intern'), ('Project Manager', 'Project Manager'), ('Frontend Developer', 'Frontend Developer'), ('Scrum Master', 'Scrum Master'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Backend Developer', 'Backend Developer')], default='Junior Developer', max_length=50),
        ),
    ]
