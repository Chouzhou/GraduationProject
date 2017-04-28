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
from student.views import *
urlpatterns = [
    # 显示课程的所有URL集合
    url(r'^allCourse_form/$', allCourseForm, name='allCourse_form'),
    url(r'^singleCourse_form/(?P<courseId>\d+)$', singleCourse, name='singleCourse_form'),
    # 作业
    url(r'^task_html/', taskForm, name='task_form'),
    url(r'^doTask_html/(?P<taskId>\d+)/', doTaskHtml, name='doTask_html'),
    # 显示成绩
    url(r'^showGrade/', showGrade, name='showGrade'),
    # 计算学习时长
    url(r'studyTime/', studyTime, name='studyTime'),
]
