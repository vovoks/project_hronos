from django.db import models


class Teacher(models.Model):
    teacher_full = models.CharField(verbose_name="ФИО полностью", max_length=255)
    teacher = models.CharField(verbose_name="ФИО", max_length=72)


class Room(models.Model):
    code = models.IntegerField(verbose_name="Код")
    name = models.CharField(verbose_name="Название", max_length=255)


class Group(models.Model):
    code = models.CharField(verbose_name="Код", max_length=255)
    name = models.CharField(verbose_name="Название", max_length=255)


class Discipline(models.Model):
    code = models.CharField(verbose_name="Код", max_length=255)
    name = models.CharField(verbose_name="Название", max_length=255)


class Class(models.Model):
    class_code = models.IntegerField(verbose_name='Код')
    name = models.CharField(verbose_name='Название', max_length=255)
    time_from = models.TimeField(verbose_name="Время начала")
    time_to = models.TimeField(verbose_name="Время окончания")


class Semestr(models.Model):
    name = models.CharField(verbose_name='Название семестра', max_length=255)
    date_start = models.DateField(verbose_name='Дата начала семестра')
    date_end = models.DateField(verbose_name='Дата начала семестра')


class WeekAlternationList(models.Model):
    # 1 - первый числитель, 2 - второй числитель, 3 - первый знаменатель, 4 - второй знаменатель
    week_code = models.PositiveIntegerField(verbose_name="Номер недели")
    alternation_code = models.PositiveIntegerField(verbose_name="Числитель/Знаменатель")
    alternation_name = models.CharField(verbose_name="Название", max_length=255)
    alternation_name_short = models.CharField(verbose_name="Короткое название", max_length=255)


class Schedule(models.Model):
    day = models.DateField(verbose_name='Дата')
    alternation_week = models.ForeignKey(WeekAlternationList, on_delete=models.DO_NOTHING,
                                         verbose_name="Числитель/знаменатель")
    class_time = models.ForeignKey(Class, on_delete=models.DO_NOTHING, verbose_name="Пара")
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, verbose_name="Группа")
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, verbose_name="Дисциплина")
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, verbose_name="Преподаватель")
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, verbose_name="Аудитория")


class FileUpload(models.Model):
    file_name = models.CharField(max_lenght=72, verbose_name="Название файла")
    file_hash = models.CharField(max_lenght=255, verbose_name="Хеш файла")
