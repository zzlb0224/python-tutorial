from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def article(request):
    return HttpResponse('文章首页')


def article_list(request, year):
    return HttpResponse('文章列表:'+year)


def article_list_month(request, month):
    return HttpResponse('文章列表:'+month)


def article_category(request, categories):
    return HttpResponse(' 分类： %s ' % (categories))
