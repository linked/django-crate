# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-18 08:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import example.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(blank=True, max_length=1024, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'in_db': 'crate',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.CharField(blank=True, max_length=1024, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('published', models.DateTimeField(default=datetime.datetime.now)),
                ('pages', models.PositiveIntegerField(blank=True, null=True)),
                ('extra', example.models.ObjectField()),
                ('tags', example.models.StringArrayField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.Author')),
            ],
            options={
                'in_db': 'crate',
            },
        ),
    ]
