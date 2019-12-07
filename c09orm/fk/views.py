from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection


from .models import *
from django.contrib.auth.models import User
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


def article(request):
    ms = Article.objects.all()
    print(ms)
    print(connection.queries)
    return HttpResponse(ms)


def categoryaddarticle(request):
    category = Category.objects.first()
    article = Article(title="aaa", content="测试add")
    article.author = User.objects.first()
    article.save()
    category.article_set.add(article, bulk=False)

    return HttpResponse('success')


def one_to_one_add_view(request):
    root = User.objects.first()
    # print(root)

    a = UserExtend(user=root, nickname='折纸')
    a.save()

    return HttpResponse('success')


def one_to_one_view(reuqest):
    ue = UserExtend.objects.first()
    print(ue.user)

    root = User.objects.first()
    print(root.userextend)
    var = root.userextend
    var.nickname = '搜索'
    var.save()
    return HttpResponse(ue)


def many_to_many_view(request):
    article = Article.objects.first()
    tag = Tag(name='热门')
    tag.save()
    article.tags.add(tag)
    return HttpResponse('success')


def tagaddarticle(request):
    tag = Tag.objects.get(pk=3)
    article = Article(title='红楼梦')
    article.save()
    tag.articles.add(article)
    return HttpResponse('success')


def m2marticle(request, id):
    article = Article.objects.get(pk=id)
    return HttpResponse([article, article.tags.all()])


def m2mtag(request, id):
    tag = Tag.objects.get(pk=id)
    return HttpResponse([tag, tag.articles.all()])


def qu(request):
