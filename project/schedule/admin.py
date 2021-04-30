from django.contrib import admin

from .models import *


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Teacher, TeacherAdmin)


class RoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)


class DisciplineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Discipline, DisciplineAdmin)

class WeekAlternationListAdmin(admin.ModelAdmin):
    pass


admin.site.register(WeekAlternationList, WeekAlternationListAdmin)

class ClassAdmin(admin.ModelAdmin):
    pass


admin.site.register(Class, ClassAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Schedule, ScheduleAdmin)