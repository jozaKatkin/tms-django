from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")


def index1(request):
    name = request.POST.get("name")
    length = len(name)
    return HttpResponse(length)


def index2(request):
    age = request.POST.get("age")
    if int(age) < 18:
        return HttpResponse("В доступе отказано")
    else:
        return HttpResponse("Добро пожаловать!")
