from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_title = "电脑安全管理系统"

admin.site.site_header = "电脑管理系统"

admin.site.index_title = "电脑信息"


@admin.register(Article2)
class Article2Admin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = '文章列表'
