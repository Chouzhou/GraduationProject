# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from .views import *
# from rest_framework import routers


urlpatterns = [
    url(r'all/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'user/(?P<user_id>.+)', UserViewSet.as_view()),
]