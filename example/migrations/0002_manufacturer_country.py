# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='country',
            field=models.CharField(default='AU', max_length=3),
            preserve_default=False,
        ),
    ]
