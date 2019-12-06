from . import views
from django.urls import path

app_name = 'fk'

urlpatterns = [
    path('', views.index)
]
