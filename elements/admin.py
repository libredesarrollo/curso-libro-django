from django.contrib import admin

from .models import Type, Category

@admin.register(Type, Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    