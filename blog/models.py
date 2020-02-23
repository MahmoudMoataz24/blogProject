from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    title = models.CharField(max_length=200)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    updated = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.title
<<<<<<< HEAD
=======

>>>>>>> be86348346c474582e9ad09972b5796ebac278da
    class Meta:
        ordering = ['-created']

class Comments(models.Model):
    content=models.TextField()
    createTime=models.DateTimeField(auto_now_add=True)
    userID=models.ForeignKey(User, on_delete=models.CASCADE)
    postID=models.ForeignKey(Post, on_delete=models.CASCADE)


class reply(models.Model):
    slug=models.SlugField(max_length=200)
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    comId=models.ForeignKey(Comments,on_delete=models.CASCADE)

class Likes(models.Model):
    userID=models.ForeignKey(User,on_delete=models.CASCADE)
    postID=models.ForeignKey(Post,on_delete=models.CASCADE)


