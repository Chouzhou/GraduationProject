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
from django.conf.urls import url, include, static
from django.contrib import admin
from blog.views import *
from django.views.static import serve
# from Social_Blog import settings
from django.conf import settings
urlpatterns = [
    # django自带的管理界面
    url(r'^admin/', admin.site.urls),
    # 账户管理界面
    url(r'^account/', include('blog.urls')),
    # 学员界面
    url(r'^student/', include('student.urls')),
    # 教师界面
    url(r'^teacher/', include('teacher.urls')),
    # 主界面
    url(r'^$', index, name='index'),
    # 自己的管理员界面
    url(r'^myAdmin/', include('MyAdmin.urls')),
    # 视频播放地址
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
