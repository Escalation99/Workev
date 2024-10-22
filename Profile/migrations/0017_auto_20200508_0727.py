# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 07:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0016_auto_20200508_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Intern', 'Intern'), ('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Junior Developer', 'Junior Developer'), ('Project Manager', 'Project Manager'), ('UI/UX Designer', 'UI/UX Designer'), ('Scrum Master', 'Scrum Master'), ('CEO', 'CEO'), ('Vice CEO', 'Vice CEO'), ('Frontend Developer', 'Frontend Developer')], default='Junior Developer', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
