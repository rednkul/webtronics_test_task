from django.contrib.auth import get_user_model
from django.db import models

from posts.models import Post
# Create your models here.

class Like(models.Model):
    LIKE_OR_DISLAKE_CHOICES = (
        ("LIKE", "like"),
        ("DISLIKE", "dislike"),
        (None, "None")
    )

    user = models.ForeignKey(get_user_model(), verbose_name='User', on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE, related_name='post_likes')
    like_or_dislike = models.CharField(max_length=7,
                                       choices=LIKE_OR_DISLAKE_CHOICES,
                                       default=None
    )

    def __str__(self):
        return f'{self.user.username}: {self.post.title} | {self.like_or_dislike}'