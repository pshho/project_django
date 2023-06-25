from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname