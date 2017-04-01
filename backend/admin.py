# -*- coding: utf-8 -*-
from django.contrib import admin
from backend.models import User
# Register your models here.
# 在未更改数据界面显示字段
@admin.register(User)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username')
# admin.site.register(Article, ArticleAdmin)