from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userAdds(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)

    canInteract = models.BooleanField()
    isAdmin = models.BooleanField()