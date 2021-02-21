# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-14 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0056_auto_20201202_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('All', 'All'), ('Scrum Master', 'Scrum Master'), ('UI/UX Designer', 'UI/UX Designer'), ('Fullstack Developer', 'Fullstack Developer'), ('Frontend Developer', 'Frontend Developer'), ('Junior Developer', 'Junior Developer'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('Project Manager', 'Project Manager'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO')], default='All', max_length=50),
        ),
    ]