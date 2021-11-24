from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentProfileSerializer ,TeacherProfileSerializer ,UserSerializer

from django.contrib.auth.models import User
from .models import StudentProfile  ,TeacherProfile
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################


class StudentProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    def retrieve(self, request, pk=None):
        queryset = User.objects.all(name = request.user)
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer   
    permission_classes = (IsAuthenticated,)
    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated] )
    def get_profile(self, request, pk=None) :
        user = User.objects.get(id = request.user.id)
        print(user.is_staff)
        print("hfawiugfautgakujefgeuIW")
        if user.is_staff == True:
            instance = TeacherProfile.objects.get(name = request.user.id)
            serializer = TeacherProfileSerializer(instance)
            return Response(serializer.data)
        else :
            instance = StudentProfile.objects.get(name = request.user.id)
            serializer = StudentProfileSerializer(instance)
            return Response(serializer.data)

            
