from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Author', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=2000)
    image = models.ImageField('Image', upload_to='images/', blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    changed_at = models.DateTimeField('Created at', auto_now=True, )

    def __str__(self):
        return f'{self.author.username}: {self.title} | {self.created_at}'