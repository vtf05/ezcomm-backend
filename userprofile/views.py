from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerailizer 

from django.contrib.auth.models import User
from .models import Profile  
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request) :
        req_user = request.user
        profile_obj = Prfile.objects.get(name = req_user)
        if profile_obj.is_Teacher  :
            return  Response(status = status.HTTP_201_CREATED)

        else :
            return  Response(status = status.HTTP_401_UNAUTHORIZED)        