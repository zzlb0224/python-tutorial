from django.urls import path
from . import views
app_name = 'book'

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('delete', views.delete),
    path('detail/<id>/', views.detail),
    path('articleadd', views.articleadd),
    path('article/<id>/', views.articledetail),
    path('car/detail/<id>/', views.cardetail, name='cardetail')
]
