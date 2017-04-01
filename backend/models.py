# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField('员工编号', primary_key=True)
    user_password = models.CharField(max_length=40, verbose_name="密码")
    username = models.CharField(max_length=80, verbose_name="员工名字")
    def __str__(self):
        return self.username

