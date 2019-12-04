from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('前台首页')


def login(request):
    return HttpResponse('前台login')
