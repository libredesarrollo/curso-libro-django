from django.contrib import admin

from .models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','text')
    search_fields = ('text', 'id')
    date_hierarchy = 'date_posted'
    ordering = ('date_posted',)
    list_filter = ('id', 'date_posted')
    list_editable = ('text',)


    #fields = ('text',)
    #exclude = ('text',)
    
#admin.site.register(Comment, CategoryAdmin)