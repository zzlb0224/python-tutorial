from django.db import models
from django.utils.timezone import timezone, now
# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return "book:{{id:{id},title:{title}}}".format(title=self.title,
                                                       id=self.id
                                                       )


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=True)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    removed = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, null=True)
