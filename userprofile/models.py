from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfile(models.Model) :

    name        = models.OneToOneField(User , on_delete = models.CASCADE)
    Profile_pic = models.ImageField()
    Roll_number = models.CharField(max_length = 15 ,unique = True)
    branch      = models.CharField(max_length = 15)
    semester    = models.CharField(max_length = 15) 

    
    def __str__(self):
        return  str(self.name)
        


class TeacherProfile(models.Model) :

    name        = models.OneToOneField(User , on_delete = models.CASCADE)
    designation = models.CharField(max_length = 30)
    Profile_pic = models.ImageField()
    is_HOD      = models.BooleanField(default = 0)
    