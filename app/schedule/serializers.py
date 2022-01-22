from rest_framework import serializers

from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['day_week_short', 'alt_week_short', 'class_time_num', 'class_time_start', 'class_time_end', 'group_name', 'discipline_name', 'teacher_name', 'room_name']