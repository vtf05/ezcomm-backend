from django.db import models
from django.contrib.auth.models import User
from userprofile.models import StudentProfile
from notice.models import Notice_Post
import datetime
# Create your models here.

class Assignment(models.Model) :
    assigned_by     =  models.ForeignKey(Notice_Post , on_delete = models.CASCADE)
    submitted_by    =  models.ForeignKey(StudentProfile , on_delete = models.CASCADE)
    subject_name    =  models.CharField(max_length = 50 )
    title           =  models.CharField(max_length = 200)
    submission_date =  models.DateTimeField(default = datetime.datetime.now())
    upload_file     =  models.FileField(upload_to ='uploads/')
    is_plagiarised  =  models.BooleanField(default = 0)
    is_submitted    =  models.BooleanField(default = 0)
    is_accepted     =  models.BooleanField(default = 0)
    marks           =  models.IntegerField(default = 0)
    

    def __str__(self) :
        return str(self.assigned_by)+"_"+str(self.submitted_by)+"_"+str(self.title)
    
