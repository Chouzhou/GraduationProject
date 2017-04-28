# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import *

# Create your views here.
# 返回添加用户的页面
def insertUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['initialPwd']
        # user = User.objects.get(username=username)
        # if user:
        #     return render(request, 'admin/insertUser.html', {'info':'用户名已经使用过'})
        if request.POST['role'] == '老师':
            print(request.POST['role'])
            role = True
            user = teacher.objects.create_user(username=username, password=password, role=role)
            user.save()
        else:
            role = False
            user = student.objects.create_user(username=username, password=password, role=role)
            user.save()
        return render(request, 'admin/insertUser.html', {'info':'添加成功'})
    else:
        return render(request, 'admin/insertUser.html')



# 重置密码
def resetPwd(request):
    if request.method == 'POST':
        resetPwd = request.POST['resetPwd']
        username = request.POST['username']
        print(username, resetPwd)
        user = User.objects.get(username=username)
        user.set_password(resetPwd)
        user.save()
        return render(request, 'admin/resetPwd.html', {'info': '重置成功'})
    else:
        return render(request, 'admin/resetPwd.html')