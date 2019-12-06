from django.db import models
from django.utils.timezone import timezone, now
# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    price = models.FloatField(default=0, blank=True)

    def __str__(self):
        return "book:{{id:{id},title:{title}}}".format(title=self.title,
                                                       id=self.id
                                                       )


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    removed = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    update_time = models.DateTimeField(auto_now=True)


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    signature = models.TextField(blank=True)
    avastar = models.URLField(blank=True)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
