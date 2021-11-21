from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Notice_Post , Comment



class Notice_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice_Post 
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comment 
        fields = '__all__'

