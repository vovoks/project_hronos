import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .loader import get_schedule
from .models import Schedule, Group
from .parser import parse_schedule
from .serializers import ScheduleSerializer


class ScheduleList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group__name', 'day', 'teacher__teacher', 'discipline__code', 'teacher__teacher', 'room__name']

    def get(self, request, *args, **kwargs):
        if "group__name" not in request.query_params.keys():
            return Response({"error": "Параметр названия группы (group__name) обязателен!"})
        return super().get(request, *args, **kwargs)


class LoadScheduleFromSite(APIView):
    swagger_schema = None
    def get(self, request, group):
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
