from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_display_links = ('author', 'title')
    list_filter = ('author',)
