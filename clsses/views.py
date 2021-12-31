from rest_framework import viewsets
from rest_framework import status , parsers
from rest_framework.permissions import IsAuthenticated
from .serializers import AssignmentSerializer , ScheduleSerializer

from django.contrib.auth.models import User
from .models import Assignment ,Schedule
from rest_framework.response import Response
from rest_framework.decorators import action
################## django api view ###################


class AssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    filter_fields = (
        'assigned_by',
    )
    parser_classes = [parsers.MultiPartParser,parsers.FormParser]

class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_fields = (
        'day','semester'
    )
    parser_classes = [parsers.MultiPartParser,parsers.FormParser]


