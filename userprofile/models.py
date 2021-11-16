from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model) :
    name = models.OneToOneField(User , on_delete = models.CASCADE)
    designation = models.CharField(max_length = 200)
    is_Teacher = models.BooleanField(default = 0)
    

    
    def __str__(self):
        return  str(self.name)
        
