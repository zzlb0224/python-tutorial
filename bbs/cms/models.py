from django.db import models

# Create your models here.
from front.models import Article


class Article2(Article):
    class Meta:
        proxy = True
        verbose_name = "文章复核"
        verbose_name_plural = '文章复核列表'
