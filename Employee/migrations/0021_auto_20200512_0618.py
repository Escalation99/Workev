# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-12 06:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0020_auto_20200512_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_sender', to=settings.AUTH_USER_MODEL)),
                ('given_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_receiver', to=settings.AUTH_USER_MODEL)),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_feedback', to='Employee.TaskReport')),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Regular Meeting', 'Regular Meeting'), ('Code Review', 'Code Review'), ('Alignment Meeting', 'Alignment Meeting'), ('Sprint Planning', 'Sprint Planning'), ('Sprint Retrospective', 'Sprint Retrospective')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('Frontend Developer', 'Frontend Developer'), ('Scrum Master', 'Scrum Master'), ('UI/UX Designer', 'UI/UX Designer'), ('Vice CEO', 'Vice CEO'), ('All', 'All'), ('Junior Developer', 'Junior Developer'), ('CEO', 'CEO'), ('Backend Developer', 'Backend Developer'), ('Intern', 'Intern'), ('Fullstack Developer', 'Fullstack Developer'), ('Project Manager', 'Project Manager')], default='All', max_length=50),
        ),
    ]
