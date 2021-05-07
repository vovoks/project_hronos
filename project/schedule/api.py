import json

from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .loader import get_schedule
from .models import Schedule, Group
from .parser import check_schedule_structure, parse_schedule


class ScheduleList(APIView):
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        schedules = [schedule.day for schedule in Schedule.objects.all()]
        return Response(schedules)


class LoadScheduleFromSite(APIView):
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, group, format=None):
        errors = []
        success = []
        schedule, schedule_errors = get_schedule(group)
        errors.extend(schedule_errors)

        group_obj = Group.objects.filter(name=group)

        if not group_obj:
            errors.append("Некорректный номер группы: {}".format(group))

        if not schedule_errors and group_obj:
            success_parse, errors_parse = parse_schedule(json.dumps(schedule))
            errors_parse.extend(errors_parse)
            success.extend(success_parse)

        return Response({"errors": errors, "success": success})
