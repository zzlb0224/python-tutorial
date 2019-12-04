from django.urls import re_path, path
from . import views
from django.urls import register_converter


class CategoryConverter(object):
    regex = r'\w+(\+\w+)*'

    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        if isinstance(value, list):
            return '+'.join(value)
        else:
            return value


register_converter(CategoryConverter, 'cate')

urlpatterns = [
    re_path(r'^$', views.article),
    re_path(r'list/(?P<year>\d{4})/', views.article_list),
    re_path(r'list/(?P<month>\d{2})/', views.article_list_month),
    path('cate/<cate:categories>/', views.article_category)
]
