# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homelessApp', '0009_auto_20170418_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomelessMigration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('migrationarea', models.CharField(max_length=255)),
                ('migrationpercent', models.FloatField()),
            ],
            options={
                'db_table': 'homelessmigration',
                'verbose_name_plural': 'Homeless Migration',
            },
        ),
    ]
