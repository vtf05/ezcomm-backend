from django.db import models
from django.contrib.auth.models import User


class Wallet (models.Model):
    user                = models.OneToOneField(User, on_delete = models.CASCADE)                
    Ammount             = models.IntegerField(default = 0)   
   
