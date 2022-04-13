from django.contrib import admin

from .models import Type, Category, Element

@admin.register(Type, Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class ElementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Element, ElementAdmin)