from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(blank=True, max_length=100)

    
    

    def __str__(self):
        return self.name
