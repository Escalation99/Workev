# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-13 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0057_auto_20200513_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('UI/UX Designer', 'UI/UX Designer'), ('Junior Developer', 'Junior Developer'), ('Vice CEO', 'Vice CEO'), ('Scrum Master', 'Scrum Master'), ('Intern', 'Intern'), ('Frontend Developer', 'Frontend Developer'), ('Project Manager', 'Project Manager'), ('Fullstack Developer', 'Fullstack Developer'), ('CEO', 'CEO'), ('Backend Developer', 'Backend Developer')], default='Junior Developer', max_length=50),
        ),
    ]