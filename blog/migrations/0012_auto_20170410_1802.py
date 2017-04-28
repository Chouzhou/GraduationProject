# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170410_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pulishId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Teacher'),
        ),
        migrations.AlterField(
            model_name='task',
            name='pulishId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Teacher'),
        ),
    ]