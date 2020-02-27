from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    title = models.CharField(max_length=200)



class Post(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tagName = models.CharField(max_length=30)
    UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image=models.ImageField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']