from django.contrib import admin

from forum.models import *


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'description']
    list_filter = ['title']
    search_fields = ['title']
    fields = ['title', 'description', 'author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_text', 'created_at', 'topic']
    list_filter = ['comment_text', 'created_at', 'topic']
    search_fields = ['comment_text', 'created_at', 'topic']
    fields = ['comment_text', 'topic', 'author']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)


