from django.contrib import admin
from blog.models import Article, Category 
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'status')
    list_filter = ('status',)
    ordering = ('-created_time',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
