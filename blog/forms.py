# -*-coding:utf-8 -*-
from django import forms



# 修改密码Ｆｏｒｍ
class ModifyPwdForm(forms.Form):
    oldPwd = forms.CharField(label="旧密码", error_messages={"required": "这个选项必须填写"})
    newPwd = forms.CharField(label="新密码", error_messages={"required": "这个选项必须填写"})
    againPwd = forms.CharField(label="再输入一次新密码", error_messages={"required": "这个选项必须填写"},widget=forms.PasswordInput)
    