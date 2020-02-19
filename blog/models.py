from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
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
>>>>>>> d8ad008f2dc602654a0c5445ac24602920316495
