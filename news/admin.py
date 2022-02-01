from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(Setting)
class AdminSetting(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'phone']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    pass
