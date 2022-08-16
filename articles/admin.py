from distutils import archive_util
from django.contrib import admin
from . import models 
# Register your models here.

class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(models.Article, ArticleAdmin)

admin.site.register(models.Comment)
