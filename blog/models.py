from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()


    def __str__(self):
        return self.title

