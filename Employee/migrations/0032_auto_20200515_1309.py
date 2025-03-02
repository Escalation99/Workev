# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-15 06:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0031_auto_20200515_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_feedback_reply_sender', to=settings.AUTH_USER_MODEL)),
                ('given_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app_feedback_reply_receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Code Review', 'Code Review'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Regular Meeting', 'Regular Meeting'), ('Alignment Meeting', 'Alignment Meeting'), ('Sprint Planning', 'Sprint Planning')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('All', 'All'), ('Project Manager', 'Project Manager'), ('Frontend Developer', 'Frontend Developer'), ('Vice CEO', 'Vice CEO'), ('Scrum Master', 'Scrum Master'), ('Backend Developer', 'Backend Developer'), ('CEO', 'CEO'), ('Fullstack Developer', 'Fullstack Developer'), ('Intern', 'Intern'), ('UI/UX Designer', 'UI/UX Designer'), ('Junior Developer', 'Junior Developer')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Online', 'Online'), ('Seminar', 'Seminar')], default='Regular', max_length=255),
        ),
    ]
