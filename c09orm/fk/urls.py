from . import views
from django.urls import path

app_name = 'fk'

urlpatterns = [
    path('', views.index),
    path('category/add/<name>/', views.addcategory),
    path('article/add/', views.addarticle)
]
