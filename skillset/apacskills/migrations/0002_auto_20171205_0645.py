# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apacskills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills_map',
            name='skill_level',
            field=models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary')], max_length=1),
        ),
    ]
