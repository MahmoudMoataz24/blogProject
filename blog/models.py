from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userAdds(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    canInteract = models.BooleanField()
    isAdmin = models.BooleanField()

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
     class Meta:
        ordering = ['-created']

class Comments(models.Model):
    content=models.TextField()
    createTime=models.DateTimeField(auto_now_add=True)
    userID=models.ForeignKey(User,models.CASCADE)
    postID=models.ForeignKey(Post,models.CASCADE)
    
class reply(models.Model):
    slug=models.SlugField(max_length=200)
    userId=models.ForeignKey(userAdds,on_delete=models.CASCADE)
    comId=models.ForeignKey(comments,on_delete=models.CASCADE)
    
class Likes(models.Model):
    userID=models.ForeignKey(userAdds,models.CASCADE)
    postID=models.ForeignKey(Post,models.CASCADE)
