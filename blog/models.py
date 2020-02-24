# from django.db import models
# from django.contrib.auth.models import User


# # Create your models here.

# class userAdds(models.Model) :
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     canInteract = models.BooleanField()
#     isAdmin = models.BooleanField()

# class Category (models.Model):
#     title = models.CharField(max_length=200)

# class Post(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200)
#     updated = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
   
#     def __str__(self):
#         return self.title
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title