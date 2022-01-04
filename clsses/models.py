from django.db import models
from django.contrib.auth.models import User
from userprofile.models import StudentProfile
from notice.models import Assignment_Post
from django.contrib.postgres.fields import ArrayField
import datetime
# Create your models here.

class Assignment(models.Model) :
    assigned_by     =  models.ForeignKey(Assignment_Post , on_delete = models.CASCADE)
    submitted_by    =  models.ForeignKey(StudentProfile  ,  on_delete = models.CASCADE)
    name            =  models.CharField(max_length = 50 , null = True , blank = True)
    submission_date =  models.DateTimeField(default = datetime.datetime.now)
    upload_file     =  models.FileField(upload_to ='uploads/')
    is_plagiarised  =  models.BooleanField(default = 0)
    is_submitted    =  models.BooleanField(default = 1)
    is_accepted     =  models.BooleanField(default = 0)
    marks           =  models.IntegerField(default = 0)
    

    def __str__(self) :
        return str(self.assigned_by)+"_"+str(self.submitted_by)
    
class TimeTable(models.Model) :
    semester        =  models.IntegerField(default=1)
    Monday          =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    Tuesday         =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)  
    Wednesday       =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    Thursday        =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    Friday          =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    Saturday        =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)


class Semester (models.Model):
   
    name    =   models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Day(models.Model):
    name    =    models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    semester      =  models.ForeignKey(Semester,on_delete = models.CASCADE)
    day           =  models.ForeignKey(Day,on_delete = models.CASCADE)
    lecture_one   =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    lecture_two   =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    lecture_three =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    lecture_four  =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    lecture_five  =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)
    lecture_six   =  ArrayField(models.CharField(max_length=30, null=True, blank=True), blank=True, null=True)


