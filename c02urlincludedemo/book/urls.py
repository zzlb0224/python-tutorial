from django.urls import path
from . import views

urlpatterns = [
    path('', views.book),
    path('list', views.book_list),
    path('detail/<book_id>/', views.book_detail)
]
