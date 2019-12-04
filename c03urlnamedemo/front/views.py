from django.shortcuts import render, redirect

from django.http import HttpResponse
# Create your views here.


def index(request):
    username = request.GET.get('username')
    if(username):
        return HttpResponse('前台首页')
    else:
        return redirect('/login/')


def login(request):
    return HttpResponse('前台login')
