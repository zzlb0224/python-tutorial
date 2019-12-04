from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def book(request):
    print(request)
    return HttpResponse('图书')


def book_list(request):
    return HttpResponse('book列表')


def book1(request, book_id):
    return HttpResponse("book:%s" % book_id)


def book2(request):
    book_id = request.GET.get('book_id')
    return HttpResponse("book:%s" % book_id)


def book_author(request):
    pass


def book_publisher_detail(request):
    pass


def book_detail(request):
    pass
