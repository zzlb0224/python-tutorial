from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    # book = Book(title="红楼梦")
    # book.save()
    books = Book.objects.all()
    print(books)
    return HttpResponse((books))


def add(request):
    book = Book(title="红楼梦", price=100)
    book.save()
    book = Book(title="西游记", price=65)
    book.save()
    book = Book(title="吴承恩", price=89)
    book.save()


def delete(request, id=1):
    book = Book.objects.get(pk=id)
    print(book)
    book.delete()
    return HttpResponse('ok')


def detail(request, id):
    book = Book.objects.get(pk=id)
    print(book)
    return HttpResponse('ok')


def articleadd(request):
    article = Article()
    article.title = 'aaa'
    article.save()
    return HttpResponse('ok')


def articledetail(request, id):
    a = Article.objects.get(pk=id)
    print(a)
    return render(request, 'index.html', context={'create_time': a.create_time})


def authorlist(request):
    authors = Author.objects.all()
    return HttpResponse('ok')


def cardetail(request, id):
    a = Car.objects.get(pk=id)
    print(a)

    return HttpResponse('ok')
