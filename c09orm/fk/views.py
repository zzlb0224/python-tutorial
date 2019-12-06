from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.


def index(request):
    print(Article.objects.all())
    return HttpResponse('ok')


def addcategory(request, name):
    Category(name=name).save()
    return HttpResponse('ok')


def category(request):
    cas = Category.objects.all()
    return HttpResponse(cas)


def addarticle(request):
    category = Category.objects.first()
    article = Article(title='abc', content='111')
    article.category = category
    article.save()
    return HttpResponse('ok')
