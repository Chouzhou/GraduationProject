# -*- coding:utf-8 -*- 
from django.shortcuts import render
from backend.models import User
from rest_framework import generics
from backend.serializers import UserSerializer
# 解决出现‘身份认证信息未提供’
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly 
# Create your views here.


class UserViewSet(generics.ListAPIView):
    # authentication_classes = (BasicAuthentication, SessionAuthentication, )  
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        # queryset = Article.objects.all()
        user_id = self.kwargs['user_id']
        if user_id is not None:
            queryset = User.objects.filter(user_id=int(user_id))
        return queryset
