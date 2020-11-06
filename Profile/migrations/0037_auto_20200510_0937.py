# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0036_auto_20200510_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Fullstack Developer', 'Fullstack Developer'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master'), ('Junior Developer', 'Junior Developer'), ('Frontend Developer', 'Frontend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('CEO', 'CEO'), ('Vice CEO', 'Vice CEO')], default='Junior Developer', max_length=50),
        ),
    ]
