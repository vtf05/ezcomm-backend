from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import StudentProfile , TeacherProfile



class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile 
        fields = '__all__'

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'
