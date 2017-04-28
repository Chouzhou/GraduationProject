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
from teacher.views import *
urlpatterns = [
    # 布置作业
    url(r'createTask/', createTask, name="createTask"),
    # 创建课程
    url(r'createCourse/', createCourse, name="createCourse"),
    # 上传视频
    url(r'uplodeVideo/', uplodeVideo, name="uplodeVideo"),
    # 显示所有作业
    url(r'^task_html/(?P<teacherId>\d+)/', taskForm, name='task_form'),
    # 查看盖作业下的所有学生作业
    url(r'^showAllAnswer/(?P<taskId>\d+)/', showAllAnswer, name='showAllAnswer'),
    # 提交分数
    url(r'^submitGrade/(?P<answerId>\d+)/', submitGrade, name='submitGrade'),
    # 查看具体答案
    url(r'^answerDetail/(?P<answerId>\d+)/', answerDetail, name='answerDetail'),
]
