from django.contrib import admin
from django.contrib.admin import ModelAdmin

from articles.models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Article)
class CustomUserAdmin(ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = [('date', admin.DateFieldListFilter)]
    search_fields = ['title', 'author']
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['comment', 'article', 'author', 'created_at']
    list_filter = [('date', admin.DateFieldListFilter)]
    search_fields = ['comment']
