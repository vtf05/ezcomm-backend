from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Notice_Post(models.Model) :

    author = models.OneToOneField(User , on_delete = models.CASCADE)
    date = models.DateTimeField()
    content = models.TextField(max_length = 300)
    image_content = models.ImageField(upload_to = 'media')
    is_assignment  =  models.BooleanField(default=False)
  




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
        