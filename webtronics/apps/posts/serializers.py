from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    changed_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'likes_count', 'dislikes_count', 'created_at', 'changed_at']

    def get_likes_count(self, obj):
        return obj.post_likes.filter(like_or_dislike="LIKE").count()

    def get_dislikes_count(self, obj):
        return obj.post_likes.filter(like_or_dislike="DISLIKE").count()
