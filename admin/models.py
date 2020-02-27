from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='Images/')
    updated = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tagName = models.CharField(max_length=30 , default='null')
    userID = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created']
    def validate_image(image):
        max_height = 1920
        max_width = 1080
        height = image.file.height 
        width = image.file.width
        if width > max_width or height > max_height:
            raise ValidationError("Height or Width is larger than what is allowed")

# class Comments(models.Model):
#     content=models.TextField()
#     createTime=models.DateTimeField(auto_now_add=True)
#     userID=models.ForeignKey(User, on_delete=models.CASCADE)
#     postID=models.ForeignKey(Post, on_delete=models.CASCADE)
class Comments(models.Model):
    postID=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    content=models.CharField(max_length=150)
    Date=models.DateTimeField(auto_now=True,auto_now_add=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering=['Date']
    def __str__(self):
        return 'Comment {}'.format(self.content)


class reply(models.Model):
    slug=models.SlugField(max_length=200)
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    comId=models.ForeignKey(Comments,on_delete=models.CASCADE)

class Likes(models.Model):
    userID=models.ForeignKey(User,on_delete=models.CASCADE)
    postID=models.ForeignKey(Post,on_delete=models.CASCADE)
    isLiked =models.BooleanField(null=True)

class forbiddenWord(models.Model):
    word=models.CharField(max_length=30)
