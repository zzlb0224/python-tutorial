from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def book(request):
    print(request)
    return HttpResponse('图书')


def book_list(request):
    return HttpResponse('book列表')
