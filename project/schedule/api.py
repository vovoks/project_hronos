import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .loader import get_schedule
from .models import Schedule, Group
from .parser import parse_schedule
from .serializers import ScheduleSerializer


class ScheduleList(generics.ListAPIView):
    #authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group__name', 'day', 'teacher__teacher']

    # def list(self, request, *args, **kwargs):
    #     return JsonResponse(self.get_serializer().data, safe=False)


class LoadScheduleFromSite(APIView):
    #authentication_classes = [authentication.BasicAuthentication]
    #permission_classes = [permissions.AllowAny]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
