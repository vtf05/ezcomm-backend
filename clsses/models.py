from django.db import models
from django.contrib.auth.models import User
from userprofile.models import StudentProfile
# Create your models here.
class Assignment(models.Model) :
    assigned_by     =  models.ForeignKey(User , on_delete = models.CASCADE)
    submitted_by    =  models.ForeignKey(StudentProfile , on_delete = models.CASCADE)
    subject_name    =  models.CharField(max_length = 50)
    title           =  models.CharField(max_length = 200)
    issue_date      =  models.DateTimeField()
    deadline        =  models.DateTimeField()
    submission_date =  models.DateTimeField()
    upload_file     =  models.FileField(upload_to ='uploads/')
    is_plagiarised  =  models.BooleanField(default = 0)
    is_submitted    =  models.BooleanField(default = 0)
    is_accepted     =  models.BooleanField(default = 0)
    marks           =  models.IntegerField(default = 0)
    

    def __str__(self) :
        return str(self.assigned_by)+"_"+str(self.submitted_by)+"_"+str(self.title)
    
