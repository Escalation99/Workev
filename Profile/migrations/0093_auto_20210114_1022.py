# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-14 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0092_auto_20201202_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Scrum Master', 'Scrum Master'), ('UI/UX Designer', 'UI/UX Designer'), ('Fullstack Developer', 'Fullstack Developer'), ('Frontend Developer', 'Frontend Developer'), ('Junior Developer', 'Junior Developer'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('Project Manager', 'Project Manager'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO')], default='Junior Developer', max_length=50),
        ),
    ]
