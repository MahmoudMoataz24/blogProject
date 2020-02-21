from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 58d75de6059ce83915648de43cc1686048b02b0a
# Create your models here.

class userAdds(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    canInteract = models.BooleanField()
    isAdmin = models.BooleanField()

class Category (models.Model):
    title = models.CharField(max_length=200)

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
<<<<<<< HEAD
    userID=models.ForeignKey(User,models.CASCADE)
=======
>>>>>>> 58d75de6059ce83915648de43cc1686048b02b0a
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    updated = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    
   
    def __str__(self):
        return self.title

class Comments(models.Model):
    content=models.TextField()
    createTime=models.DateTimeField(auto_now_add=True)
    userID=models.ForeignKey(User,models.CASCADE)
    postID=models.ForeignKey(Post,models.CASCADE)

class Likes(models.Model):
    userID=models.ForeignKey(userAdds,models.CASCADE)
    postID=models.ForeignKey(Post,models.CASCADE)


=======
   
    def __str__(self):
        return self.title
>>>>>>> d8ad008f2dc602654a0c5445ac24602920316495
>>>>>>> 58d75de6059ce83915648de43cc1686048b02b0a
