# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 03:46
from __future__ import unicode_literals

import django.contrib.postgres.fields.ranges
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homelessApp', '0003_auto_20170303_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acsid', models.CharField(blank=True, max_length=1000, null=True)),
                ('geoid', models.CharField(blank=True, max_length=255, null=True)),
                ('age', django.contrib.postgres.fields.ranges.IntegerRangeField(null=True)),
                ('count', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sourcefile', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'acsage',
            },
        ),
        migrations.CreateModel(
            name='Acsdisability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acsid', models.CharField(blank=True, max_length=1000, null=True)),
                ('geoid', models.CharField(blank=True, max_length=255, null=True)),
                ('disability_status', models.CharField(blank=True, max_length=50, null=True)),
                ('count', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sourcefile', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'acsdisability',
            },
        ),
        migrations.CreateModel(
            name='Acsrace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acsid', models.CharField(blank=True, max_length=1000, null=True)),
                ('geoid', models.CharField(blank=True, max_length=255, null=True)),
                ('race', models.CharField(blank=True, max_length=50, null=True)),
                ('count', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sourcefile', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'acsrace',
            },
        ),
        migrations.CreateModel(
            name='Acsveteran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acsid', models.CharField(blank=True, max_length=1000, null=True)),
                ('geoid', models.CharField(blank=True, max_length=255, null=True)),
                ('veteran_status', models.CharField(blank=True, max_length=50, null=True)),
                ('count', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sourcefile', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'acsveteran',
            },
        ),
    ]
