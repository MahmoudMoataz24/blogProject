from django.db import models
from django.contrib.auth.models import User

# Create your models here.
<<<<<<< HEAD

=======
class userAdds(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)

    canInteract = models.BooleanField()
    isAdmin = models.BooleanField()
>>>>>>> 4d1b390ce6a679b2f755722b37db6966ab2a4cb3
