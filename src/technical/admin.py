from django.contrib import admin
from .models import Message, Document, Documents


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipient', 'created_at', 'published_at', 'document')
    list_filter = ('created_at', 'published_at', 'author', 'recipient')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'type', 'author', 'created_at')
    search_fields = ('file_name', 'type', 'author__username')
    list_filter = ('type', 'created_at')
    ordering = ('-created_at',)

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'type', 'author', 'created_at')
    search_fields = ('file_name', 'type', 'author__username')
    list_filter = ('type', 'created_at')
    ordering = ('-created_at',)