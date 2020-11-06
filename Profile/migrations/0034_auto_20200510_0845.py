# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0033_auto_20200510_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('UI/UX Designer', 'UI/UX Designer'), ('CEO', 'CEO'), ('Fullstack Developer', 'Fullstack Developer'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master'), ('Frontend Developer', 'Frontend Developer'), ('Vice CEO', 'Vice CEO'), ('Backend Developer', 'Backend Developer'), ('Junior Developer', 'Junior Developer'), ('Intern', 'Intern')], default='Junior Developer', max_length=50),
        ),
    ]
