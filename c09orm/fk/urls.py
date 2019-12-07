from . import views
from django.urls import path

app_name = 'fk'

urlpatterns = [
    path('', views.index),
    path('category/add/<name>/', views.addcategory),
    path('article/add/', views.addarticle),
    path('article/', views.article),
    path('category/', views.category),
    path('categoryaddarticle/', views.categoryaddarticle),
    path('1to1add/', views.one_to_one_add_view),
    path('1to1/', views.one_to_one_view),
    path('m2m/add/',views.many_to_many_view)
]
