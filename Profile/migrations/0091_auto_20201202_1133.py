# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-02 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0090_auto_20201202_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Vice CEO', 'Vice CEO'), ('Intern', 'Intern'), ('Project Manager', 'Project Manager'), ('CEO', 'CEO'), ('Fullstack Developer', 'Fullstack Developer'), ('Frontend Developer', 'Frontend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Junior Developer', 'Junior Developer'), ('Backend Developer', 'Backend Developer'), ('Scrum Master', 'Scrum Master')], default='Junior Developer', max_length=50),
        ),
    ]
