# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
# 额外需要导入的模块
from django.views.decorators.csrf import csrf_exempt
from blog.models import *
# from django.contrib.auth import logout, login, authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog.forms import ModifyPwdForm
# Create your views here.

# 主页


# @login_required
def index(request):
    # session获取用户id
    if request.user.is_authenticated():
        return render(request, 'index.html', {'user': request.user})
    return render_to_response('index.html')
# 登录


def login_form(request):
    return render(request, 'login.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # try:       
        user = auth.authenticate(username=username, password=password)
        if not user:
            return render(request, 'login.html', {'info': '密码错误或者用户名错误'})
        # 验证用户是否激活
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'info': '未激活账户请联系管理员'})
    return render(request, 'login.html')


# 修改密码


@login_required
def modify_pwd(request):
    if request.method == 'GET':
        ModifyPwd_Form = ModifyPwdForm()
        return render(request, 'modifyPwd.html', {'form': ModifyPwd_Form})
    else:
        ModifyPwd_Form = ModifyPwdForm(request.POST)
        if ModifyPwd_Form.is_valid():
            oldPwd = ModifyPwd_Form.cleaned_data['oldPwd']
            username = request.user.username           
            user = auth.authenticate(username=username, password=oldPwd)
            if user and user.is_active:
                newPwd = ModifyPwd_Form.cleaned_data['newPwd']
                user.set_password(newPwd)
                user.save()
                return render(request, 'index.html', {'info': '修改密码成功'})
            else:
                return render(request, 'modifyPwd.html', {'info': '输入的旧密码错误','form': ModifyPwd_Form})



# 个人信息


@login_required
def personalInfo(request):
    if request.method == 'GET':
        return render(request, 'personalInfo.html', {'user': request.user})
    else:
        user = User.objects.get(id=request.user.id)
        if user and user.is_active:
            user.username = request.POST['username']
            user.email = request.POST['email']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.gender = request.POST['gender']
            user.mobile = request.POST['mobile']
            user.describe = request.POST['describe']
            user.save()
            return render(request, 'personalInfo.html', {'info': '修改成功','user':user})


# 退出登录


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/account/login_form/')
