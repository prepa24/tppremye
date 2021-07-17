from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import User


# Create your models here.
class User(AbstractUser):
    pass


class Bank(models.Model):
    direkte=models.ForeignKey(User, on_delete=models.CASCADE)
    dat=models.DateTimeField()
    syej=models.CharField()
    kapital=models.CharField()

class Sikisal(models.Model):
    nom=models.CharField()
    dat=models.DateTimeField()
    sikisal=models.ForeignKey(Bank, on_delete=models.CASCADE)
