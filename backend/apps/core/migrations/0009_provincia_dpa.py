# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2021-12-24 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211224_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='provincia',
            name='dpa',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]