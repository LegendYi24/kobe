from django.contrib.staticfiles.finders import find
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import Context

from app1 import models
from app1.models import student, User


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())
class registForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())
    password1 = forms.CharField(label='密__码', widget=forms.PasswordInput())

def regist(request):
    if request.method == 'POST':
        uf = registForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password1 = uf.cleaned_data['password1']
            if password != password1:
                return render_to_response('error_2.html')
            user = User.objects.filter(username=username)
            if user:
                return render_to_response('error_1.html')
            if len(user) == 0:
                info = '注册成功!'
                user = User()
                user.username = username
                user.password = password
                user.save()
                return render_to_response('success.html')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf})
def login(request):#登录
        if request.method == 'POST':
            uf = UserForm(request.POST)
            if uf.is_valid():
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                user = User.objects.filter(username=username)
                if user:
                    passwd = User.objects.filter(username=username, password=password)
                    if passwd:
                       return HttpResponseRedirect("/app1/url_hello/")
                    else:
                        return render_to_response('error_3.html')
                elif len(user) == 0:
                    return render_to_response('error_4.html')
                else:
                    return HttpResponse('0')
        else:
            uf = UserForm()
        return render_to_response('login.html', {'uf': uf})


def hello(request):
    return render_to_response('hello.html')

    return  render_to_response('show.html',locals())
def addstu(request):
    if request.method=="POST":
        Name = request.POST.get("Name", None)
        Number = request.POST.get("Number", None)
        Age = request.POST.get("Age", None)
        Origin = request.POST.get("Origin", None)
        Learn = request.POST.get("Learn", None)
        Class = request.POST.get("Class", None)
        if 1==1:
            bb = student()
            bb.Name = Name
            bb.Number = Number
            bb.Age = Age
            bb.Origin = Origin
            bb.Learn = Learn
            bb.Class= Class
            bb.save()
            return HttpResponseRedirect("/app1/url_hello/")
    return render_to_response('done.html')


def checkstu(request):#查询
    stu = student.objects.all()
    dict_student = {}
    dict_student['studentlist'] = stu
    if request.method == "POST":

        Name = request.POST.get("name", None)
        dict_student = student.objects.filter(Name=Name)
        if dict_student:
            return render_to_response("show.html",{"c":dict_student})
        else:
            return HttpResponse("查询不到此人")
    return render_to_response('check.html',dict_student)

def studentinfo(request, id):
    stu = student.objects.get(id=id)
    dict_student = {}
    dict_student['name'] = stu.Name
    dict_student['number'] = stu.Number
    dict_student['age'] = stu.Age
    dict_student['origin'] = stu.Origin
    dict_student['learn'] = stu.Learn
    dict_student['class'] = stu.Class
    c=[stu.Name,stu.Number,stu.Age,stu.Origin,stu.Learn,stu.Class]
    return render_to_response('show.html',locals())

def deletestu(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        user = student.objects.filter(Name=name)
        if user:
            models.student.objects.filter(Name=name).delete()
            return HttpResponseRedirect("/app1/url_hello/")
        else:
            return HttpResponse("查询不到此人")
    return render_to_response('delet.html')


def rewirte_1(request):#查询
    if request.method == "POST":
        Name = request.POST.get("name", None)
        dict_student = student.objects.filter(Name=Name)
        if dict_student:
            return render_to_response("rewiter.html",{"b":dict_student})
        else:
            return HttpResponse("查询不到此人")
    return render_to_response('rewiter_1.html')


def rewirte(request):#更改信息
    if request.method == "POST":
        name2 = request.POST.get("name", None)
        name = request.POST.get("name1", None)
        number = request.POST.get("number", None)
        age = request.POST.get("age", None)
        origin = request.POST.get("origin", None)
        learn = request.POST.get("learn", None)
        Class = request.POST.get("class", None)
        stu = models.student.objects.filter(Name=name2)
        if stu:
            a = models.student.objects.get(Name=name2)
            if name!="":
                a.Name = name
            if number!="":
                a.Number = number
            if age!="":
                a.Age = age
            if origin!="":
                a.Origin = origin
            if learn!="":
                a.Learn = learn
            if Class!="":
                a.Class = Class
            a.save()
            return HttpResponseRedirect("/app1/url_hello/")
        else:
            return HttpResponse("没有此人")
    return render_to_response('rewiter.html')

