from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Lead(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

class Agent(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)