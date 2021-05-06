from django.db import models


class Teacher(models.Model):
    teacher_full = models.CharField(verbose_name="ФИО полностью", max_length=255)
    teacher = models.CharField(verbose_name="ФИО", max_length=72)

    def __str__(self):
        return self.teacher

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Room(models.Model):
    code = models.IntegerField(verbose_name="Код")
    name = models.CharField(verbose_name="Название", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"


class Group(models.Model):
    code = models.CharField(verbose_name="Код", max_length=255)
    name = models.CharField(verbose_name="Название", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Discipline(models.Model):
    code = models.CharField(verbose_name="Код", max_length=255)
    name = models.CharField(verbose_name="Название", max_length=255)
    form = models.CharField(verbose_name="Форма проведения", max_length=255)

    def __str__(self):
        return "{} {}".format(self.name, self.form)

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"


class Semestr(models.Model):
    name = models.CharField(verbose_name='Название семестра', max_length=255)
    date_start = models.DateField(verbose_name='Дата начала семестра')
    date_end = models.DateField(verbose_name='Дата начала семестра')

    def __str__(self):
        return "{}: {} - {}".format(self.name,
                                    self.date_start.strftime("%d.%m.%y"),
                                    self.date_end.strftime("%d.%m.%y"))

    class Meta:
        verbose_name = "Семетр"
        verbose_name_plural = "Семестры"


class WeekAlternationList(models.Model):
    # 1 - первый числитель, 2 - второй числитель, 3 - первый знаменатель, 4 - второй знаменатель
    alternation_code = models.PositiveIntegerField(verbose_name="Числитель/Знаменатель")
    alternation_name = models.CharField(verbose_name="Название", max_length=255)
    alternation_name_short = models.CharField(verbose_name="Короткое название", max_length=255)

    def __str__(self):
        return self.alternation_name

    class Meta:
        verbose_name = "Неделя"
        verbose_name_plural = "Недели"


class Times(models.Model):
    # {"Time": "1 пара", "Code": 1, "TimeFrom": "0001-01-01T09:00:00", "TimeTo": "0001-01-01T10:30:00"
    time_name = models.CharField(max_length=72, verbose_name="Пара")
    time_code = models.PositiveIntegerField(verbose_name="Код")
    time_start = models.TimeField(verbose_name="Время начала")
    time_end = models.TimeField(verbose_name="Время окончания")

    def __str__(self):
        return "{}: {} - {}".format(self.time_name,
                                    self.time_start.strftime("%H:%M"),
                                    self.time_end.strftime("%H:%M"))

    class Meta:
        verbose_name = "Пара"
        verbose_name_plural = "Пары"


class Schedule(models.Model):
    day = models.IntegerField(verbose_name='День недели')
    alternation_week = models.ForeignKey(WeekAlternationList, on_delete=models.DO_NOTHING,
                                         verbose_name="Числитель/знаменатель")
    class_time = models.ForeignKey(Times, on_delete=models.DO_NOTHING, verbose_name="Пара")
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, verbose_name="Группа")
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, verbose_name="Дисциплина")
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, verbose_name="Преподаватель")
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, verbose_name="Аудитория")

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"

    @property
    def day_week(self):
        return ["", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"][int(self.day)]

    @property
    def day_week_short(self):
        return ["", " Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"][int(self.day)]


class FileUpload(models.Model):
    file_name = models.CharField(max_length=72, verbose_name="Название файла")
    file_hash = models.CharField(max_length=255, verbose_name="Хеш файла")

    def __str__(self):
        return "{} {}".format(self.file_name, self.file_hash)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
