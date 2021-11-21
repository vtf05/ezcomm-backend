from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Assignment



class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


