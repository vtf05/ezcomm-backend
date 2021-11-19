from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import AssignmentSerializer

from django.contrib.auth.models import User
from .models import Assignment
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################


class AssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

      