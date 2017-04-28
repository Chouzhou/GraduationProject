# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import *
import json
# Create your views here.
# 默认显示全部课程
def allCourseForm(request):
    courses = Course.objects.all()

    return render(request, 'student/allCourse.html', {'courses': courses})
# 显示单个课程的所有内容
def singleCourse(request, courseId, video=None):
    videoes = Video.objects.filter(course_id=courseId)
    course = Course.objects.get(id=courseId)
    return render(request, 'student/singleCourse.html', {'videoes': videoes, 'courseName': course.courseName})
# 显示所有作业
def taskForm(request):
    tasks = Task.objects.all()
    return render(request, 'student/task.html', {'tasks': tasks})
# 显示提交作业页面
def doTaskHtml(request, taskId):
    task = Task.objects.get(id=taskId)
    if request.method == 'POST':
        taskContent = request.POST['taskContent']
        print(taskContent)
        answer = Answer(
            answer=taskContent,
            studentDo_id = request.user.id,
            task_id = taskId,
        )
        answer.save()
        return render(request, 'student/doTask.html', {'task': task, 'info': '提交成功', 'answer': taskContent})
    else:
        return render(request, 'student/doTask.html', {'task':task})

# 显示成绩
def showGrade(request):
    answer = Answer.objects.get(studentDo_id=request.user.id)
    return render(request, 'student/grade.html', {'answer': answer})


# 计算学习时间
def studyTime(request):
    user = None
    if request.POST['currentTime']:
        useremail = request.POST['currentTime']
        print(useremail)
        result = {}
        # user = User.objects.filter(useremail__iexact = useremail)
    if user:
        result = "1"
        result = json.dumps(result)
    else:
        result = "0"
        result = json.dumps(result)
    return HttpResponse(result)
    
    