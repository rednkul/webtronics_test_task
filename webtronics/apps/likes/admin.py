from django.contrib import admin
from .models import Like
# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    list_filter = ('user', 'post', 'like_or_dislike')
    list_display_links = ('user', 'post')