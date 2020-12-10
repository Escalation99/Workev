# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-02 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0055_auto_20201202_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackreply',
            name='feedback',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_user', to='Employee.Feedback'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Alignment Meeting', 'Alignment Meeting'), ('Regular Meeting', 'Regular Meeting'), ('Code Review', 'Code Review'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Sprint Planning', 'Sprint Planning')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('Scrum Master', 'Scrum Master'), ('Junior Developer', 'Junior Developer'), ('Project Manager', 'Project Manager'), ('Frontend Developer', 'Frontend Developer'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO'), ('UI/UX Designer', 'UI/UX Designer'), ('Intern', 'Intern'), ('All', 'All')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Online', 'Online'), ('Seminar', 'Seminar'), ('Regular', 'Regular')], default='Regular', max_length=255),
        ),
    ]
