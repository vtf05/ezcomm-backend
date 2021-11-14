from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import Notice_PostSerializer , CommentSerializer

from django.contrib.auth.models import User
from .models import Notice_Post , Comment
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################


class Notice_PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Notice_Post.objects.all()
    serializer_class = Notice_PostSerializer

      

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

            
        
    

    
    

