# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
