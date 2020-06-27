from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'publish', 'created_at', 'tags')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'body',)
    ordering = ['created_at']
