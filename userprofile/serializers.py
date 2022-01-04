from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import StudentProfile , TeacherProfile



class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile 
        fields = '__all__'
        depth = 1

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = '__all__'
        depth = 1



class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'
