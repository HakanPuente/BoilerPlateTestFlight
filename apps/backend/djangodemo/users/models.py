from django.db import models

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    fav_color = models.CharField(max_length=255)

    def __str__(self):
        return self.email
