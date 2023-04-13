# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minecode', '0013_auto_20170807_0511'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='resourceuri',
            index=models.Index(fields=['-priority', 'rank'], name='minecode_r_priorit_daf7b6_idx'),
        ),
    ]