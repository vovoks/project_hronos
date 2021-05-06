from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Schedule


class ScheduleList(APIView):
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        schedules = [schedule.day for schedule in Schedule.objects.all()]
        return Response(schedules)