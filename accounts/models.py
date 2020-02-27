from django.contrib.auth.models import User
from django.db import models


class userState(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.is_blocked)