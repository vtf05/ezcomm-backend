from django.contrib import admin
from .models import  Notice_Post , Comment , Assignment_Post
# Register your models here.
admin.site.register(Notice_Post)
admin.site.register(Assignment_Post)
admin.site.register(Comment)


