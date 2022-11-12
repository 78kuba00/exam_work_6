from django.contrib import admin
from webapp.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'message', 'created_at', 'updated_at']
    list_display_links = ['author']
    list_filter = ['created_at']
    search_fields = ['author', 'message']
    exclude = []
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Comment, CommentAdmin)