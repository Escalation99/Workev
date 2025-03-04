# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 06:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0014_auto_20200508_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(choices=[('Fullstack Developer', 'Fullstack Developer'), ('Project Manager', 'Project Manager'), ('CEO', 'CEO'), ('Scrum Master', 'Scrum Master'), ('Vice CEO', 'Vice CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('Junior Developer', 'Junior Developer'), ('Frontend Developer', 'Frontend Developer')], default='Junior Developer', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
