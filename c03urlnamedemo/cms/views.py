from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse
# Create your views here.


def index(request):
    username = request.GET.get('username')
    if(username):
        return HttpResponse('前台首页')
    else:
        return redirect(reverse('%s:login' % request.resolver_match.namespace))


def login(request):
    return HttpResponse('cmslogin')
