# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170410_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(blank=True, max_length=20, null=True, verbose_name='课程名')),
                ('courseDesc', models.CharField(blank=True, max_length=20, null=True, verbose_name='课程简述')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': '课程',
                'verbose_name': '课程',
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='pulishId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Teacher'),
        ),
    ]