#-*- coding:utf-8 -*-
from django.shortcuts import render
from blog.models import *
import os
from Social_Blog import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
# 发布作业
@login_required
def createTask(request):
    if request.method == 'POST':
        if request.user.role  == True:
            taskName = request.POST['taskname']
            taskDesc = request.POST['describe']
            task = Task(
                taskName=taskName,
                taskDesc=taskDesc,
                taskPub_id=request.user.id,
            )
            task.save()
            return render(request, 'teacher/insertTask.html')
    else:
        return render(request, 'teacher/insertTask.html')

# 创建课程
@login_required
def createCourse(request):
    if request.method == 'POST':
        if request.user.role == True:
            courseName = request.POST['coursename']
            courseDesc = request.POST['describe']
            course = Course(
                courseName=courseName,
                courseDesc=courseDesc,
                coursePub_id=request.user.id,
            )
            # 创建存放视频目录
            videoDir = os.path.join(settings.BASE_DIR,'media','videoes')
            print(videoDir)
            os.mkdir(videoDir + '/' + courseName)
            course.save()
            return render(request, 'teacher/uplodeCourse.html')
    else:
        return render(request, 'teacher/uplodeCourse.html')

# 上传视频
@login_required
def uplodeVideo(request):
    courses = Course.objects.filter(coursePub_id=request.user.id)
    if request.method == 'POST':
        #　获取课程ＩＤ
        courseid = request.POST['courseid']
        course = Course.objects.get(id=courseid)
        videoName = request.POST['videoname']
        videoDesc = request.POST['describe']
        # 获取上传文件
        source = request.FILES.get('myfile', None)
        if not source:
            return render(request, 'teacher/uplodeVideo.html', {'courses': course, 'info': '上传失败'})
        else:
            videoDir = os.path.join(settings.BASE_DIR, 'media', 'videoes', course.courseName)
            filename = os.path.join(videoDir,videoName + '.mp4')
            filesrc = os.path.join('/', 'media', 'videoes', course.courseName, videoName + '.mp4')
            videoStore(filename, source)
            video = Video(
                videoName = videoName,
                videoDesc = videoDesc,
                videoSrc = filesrc,
                course_id = courseid,
            )
            video.save()
            return render(request, 'teacher/uplodeVideo.html', {'courses': courses})
    else:
        return render(request, 'teacher/uplodeVideo.html', {'courses': courses})
# 存储视频
# 异步未完成
def videoStore(filename, src): 
    with open(filename, 'wb') as fobj:
        for chrunk in src.chunks():
            fobj.write(chrunk)



# 显示该老师布置的所有作业
@login_required
def taskForm(request, teacherId):
    tasks = Task.objects.filter(taskPub_id=teacherId)
    return render(request, 'teacher/checkTask.html', {'tasks': tasks})




# 查看盖作业下的所有学生作业
@login_required
def showAllAnswer(request, taskId):
    answers = Answer.objects.filter(task_id=taskId)
    # answer = Answer.objects.get(task_id=taskId)
    # print(answer.studentDo)
    return render(request, 'teacher/showAllAnswer.html', {'answers': answers})

# 提交成绩
@login_required
def submitGrade(request, answerId):
    if request.method == 'POST':
        grade = request.POST['grade']
        print(grade)
        answer = Answer.objects.get(id=answerId)
        answer.grade = grade
        answer.save()
        return HttpResponseRedirect('/teacher/showAllAnswer/' + str(answer.task.id))

#　查看具体答案
def answerDetail(request, answerId):
    answer = Answer.objects.get(id=answerId)
    return render(request, 'teacher/answerDetail.html', {'answer': answer})
