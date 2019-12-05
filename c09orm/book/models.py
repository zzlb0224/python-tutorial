from django.db import models

# Create your models here.


class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=0, null=False)


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=True)
