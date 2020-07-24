from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # image
    thumb = models.ImageField(default='default.jpg', blank=True)

    # foreign key
    author = models.ForeignKey(User, default='1', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
