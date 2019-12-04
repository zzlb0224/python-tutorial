from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path(r'^$', views.article),
    re_path(r'list/(?P<year>\d{4})/', views.article_list),
    re_path(r'list/(?P<month>\d{2})/', views.article_list_month),
    path('cate/<cate:categories>/', views.article_category)
]
