"""c09orm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from .settings import STATIC_ROOT
# from filebrowser.sites import site


urlpatterns = [
    # path('froala_editor/', include('froala_editor.urls')),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    # path('admin/filebrowser/', site.urls),
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    # path('tinymce/', include('tinymce.urls')),
    path('book/', include('book.urls', 'book')),
    path('fk/', include('fk.urls', 'fk'))
]
