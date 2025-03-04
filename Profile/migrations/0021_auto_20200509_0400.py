# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-09 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0020_auto_20200509_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Vice CEO', 'Vice CEO'), ('Scrum Master', 'Scrum Master'), ('UI/UX Designer', 'UI/UX Designer'), ('Project Manager', 'Project Manager'), ('Intern', 'Intern'), ('Junior Developer', 'Junior Developer'), ('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('CEO', 'CEO')], default='Junior Developer', max_length=50),
        ),
    ]
