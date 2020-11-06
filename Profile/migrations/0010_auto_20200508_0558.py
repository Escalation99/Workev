# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 05:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_auto_20200508_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('Junior Developer', 'Junior Developer'), ('Project Manager', 'Project Manager'), ('Scrum Master', 'Scrum Master'), ('Fullstack Developer', 'Fullstack Developer'), ('Intern', 'Intern'), ('UI/UX Designer', 'UI/UX Designer'), ('CEO', 'CEO'), ('Vice CEO', 'Vice CEO'), ('Backend Developer', 'Backend Developer'), ('Frontend Developer', 'Frontend Developer')], default='Junior Developer', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]