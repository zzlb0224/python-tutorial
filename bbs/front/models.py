from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = '分类列表'


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = '文章列表'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True)
    origin_comment = models.ForeignKey(
        'self', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = '评论列表'
