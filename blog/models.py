# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.

# 基本用户表


class User(AbstractUser):
    mobile = models.CharField(
        max_length=11, blank=True, null=False, verbose_name='手机号码')
    describe = models.CharField(
        max_length=100, blank=True, null=False, verbose_name='自我简介')
    gender = models.CharField(
        max_length=100, blank=True, null=False, verbose_name='性别')
    is_active = models.BooleanField(default=True)
    # True代表教师 False代表学生
    role = models.BooleanField(null=False, default=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']



# 学生表
class Student(User):
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name
        ordering = ['id']





# 教师表
class Teacher(User):
    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
        ordering = ['id']




# 作业


class Task(models.Model):
    taskName = models.CharField(max_length=20, blank=True, null=True, verbose_name='作业标题')
    taskDesc = models.CharField(max_length=100, blank=True, null=True, verbose_name='作业内容')
    # 发布的老师id
    taskPub = models.ForeignKey(Teacher)



    class Meta:
        verbose_name = '作业'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.taskName



# 课程
class Course(models.Model):
    courseName = models.CharField(max_length=20, blank=True, null=True, verbose_name='课程名')
    courseDesc = models.CharField(max_length=100, blank=True, null=True, verbose_name='课程简述')
    # 发布的老师id
    coursePub = models.ForeignKey(Teacher)



    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.courseName


# 作业答案
class Answer(models.Model):
    answer = models.TextField(blank=True, null=True, verbose_name='答案')
    # 谁做的作业id
    studentDo = models.ForeignKey(Student)
    task = models.ForeignKey(Task)
    grade = models.IntegerField(null=True)


    class Meta:
        verbose_name = '答案'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.answer

class Video(models.Model):
    videoName = models.CharField(max_length=20, blank=True, null=True, verbose_name='视频名')
    videoDesc = models.CharField(max_length=20, blank=True, null=True, verbose_name='视频简述')
    videoSrc = models.CharField(max_length=100, blank=True, null=True, verbose_name='视频地址')
    # 发布的课程id
    course = models.ForeignKey(Course)