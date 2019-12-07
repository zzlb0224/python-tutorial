from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection
# Create your views here.


def index(request):
    return HttpResponse('success')


def exact(request, id=1):
    a = Article.objects.get(id__exact=id)
    print(a)
    # print(a.query)
    print(connection.queries[-1])
    b = Article.objects.filter(id__exact=id)
    print(b)
    print(b.query)
    print(connection.queries[-1])
    a = Article.objects.filter(content__exact=None)
    print(a.count())
    print(connection.queries[-1])
    try:
        c = Article.objects.get(content__exact=None)
        print(c)
        print(connection.queries[-1])
    except Article.DoesNotExist as e:
        print(e)

    return HttpResponse(a)


def iexact(request, id=1):
    a = Article.objects.filter(title__iexact=id)
    print('='*30)
    print(a)
    print(connection.queries[-1])
    print('='*30)
    return HttpResponse('ok')
