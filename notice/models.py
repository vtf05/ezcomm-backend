from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.
class Notice_Post(models.Model) :

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length = 50,null = True)
    desig =  models.CharField(max_length = 50,null = True)
    subject = models.TextField(max_length = 300,null = True)
    date = models.DateTimeField( default=timezone.now())
    content = models.TextField(max_length = 300,null=True, blank = True )
    image_content = models.ImageField(upload_to = 'images/',null=True, blank = True)
    is_assignment  =  models.BooleanField(default=False)
    template_docx = models.FileField(upload_to='files/', null=True, blank = True , verbose_name="")


class Assignment_Post(models.Model):
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length = 50,null = True)
    desig =  models.CharField(max_length = 50,null = True)
    subject = ArrayField(models.CharField(max_length=15, null=True, blank=True), blank=True, null=True)
    date = models.DateTimeField(default=timezone.now())
    title =  models.CharField(max_length = 50,null = True)
    content = models.TextField(max_length = 300)
    image_content = models.ImageField(upload_to = 'images/',null=True, blank = True)
    template_docx = models.FileField(upload_to='files/', null=True, blank = True , verbose_name="")


    

class Comment(models.Model):

    post = models.ForeignKey(Notice_Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)    
        