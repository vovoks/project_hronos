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