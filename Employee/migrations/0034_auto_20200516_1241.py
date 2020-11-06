# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-16 05:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0033_auto_20200515_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_leave_sender', to=settings.AUTH_USER_MODEL)),
                ('given_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_leave_receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='meeting',
            name='category',
            field=models.CharField(choices=[('Alignment Meeting', 'Alignment Meeting'), ('Sprint Retrospective', 'Sprint Retrospective'), ('Sprint Planning', 'Sprint Planning'), ('Code Review', 'Code Review'), ('Regular Meeting', 'Regular Meeting')], default='Regular Meeting', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='division',
            field=models.CharField(choices=[('All', 'All'), ('Intern', 'Intern'), ('Fullstack Developer', 'Fullstack Developer'), ('Vice CEO', 'Vice CEO'), ('CEO', 'CEO'), ('Junior Developer', 'Junior Developer'), ('Scrum Master', 'Scrum Master'), ('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('UI/UX Designer', 'UI/UX Designer'), ('Project Manager', 'Project Manager')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='type',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Regular', 'Regular'), ('Online', 'Online')], default='Regular', max_length=255),
        ),
    ]