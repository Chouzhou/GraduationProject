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
from MyAdmin.views import *
urlpatterns = [
    url(r'^insertUser/', insertUser, name='insertUser'),
    url(r'^resetPwd/', resetPwd, name='resetPwd'),
]