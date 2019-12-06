from django.contrib import admin

# Register your models here.

from .models import *

# Register your models here.
admin.site.register([Article,  Comment])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
