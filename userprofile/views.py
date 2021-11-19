from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentProfileSerializer ,TeacherProfileSerializer 

from django.contrib.auth.models import User
from .models import StudentProfile  ,TeacherProfile
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################


class StudentProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class TeacherProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer


    # def create(self, request) :
    #     req_user = request.user
    #     profile_obj = Prfile.objects.get(name = req_user)
    #     if profile_obj.is_Teacher  :
    #         return  Response(status = status.HTTP_201_CREATED)

    #     else :
    #         return  Response(status = status.HTTP_401_UNAUTHORIZED)        