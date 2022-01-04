from django.contrib import admin
from . models import Assignment , Semester , Day ,Schedule
# Register your models here.

admin.site.register(Assignment)
admin.site.register(Semester)
admin.site.register(Day)
admin.site.register(Schedule)