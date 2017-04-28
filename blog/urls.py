# -*- coding:utf-8 -*-
"""Social_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
# from blog.views import login_form, register_form, login, register, logout, verify_email, verify_resetPwd_email, resetPwd_email, reset_pwd
from blog.views import *
urlpatterns = [
    # 登录
    url(r'^login_form/', login_form, name='login_form'),
    url(r'^login/', login, name='login'),
    # 登出
    url(r'^logout/', logout, name='logout'),
    # 修改密码
    url(r'^modify_pwd/', modify_pwd, name='modify_pwd'),
    # 个人信息
    url(r'^personalInfo/', personalInfo, name='per_Info'),
]
