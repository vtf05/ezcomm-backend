from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Assignment , Schedule



class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__' 



