from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def book(request):
    return HttpResponse('首页')


def book_list(request):
    return HttpResponse('列表')


def book_detail(request, book_id):
    return HttpResponse('详情:'+book_id)
