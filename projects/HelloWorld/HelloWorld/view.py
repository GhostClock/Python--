# from django.http import HttpResponse
from django.shortcuts import render

# def hello(requset):
#     # return HttpResponse("Hello world")


def hello(request):
    context = {}
    context['hello'] = "Hello World"
    return render(request,'hello.html',context)