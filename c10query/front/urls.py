from django.urls import path
from . import views
app_name = 'front'


urlpatterns = [
    path('', views.index),
    path('exact/<id>/', views.exact),
    path('iexact/<id>/', views.iexact)
]
