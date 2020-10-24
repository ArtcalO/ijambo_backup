from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from . models import *

class Profil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="profil/avatars/")
    
    def __str__(self):
        return f"{self.user.username}"