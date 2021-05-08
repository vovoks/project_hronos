import json
from .models import *


def check_schedule_structure(parsed_json):
    errors = []
    success = []
    struct = {"Times": [{"Time": "", "Code": "", "TimeFrom": "", "TimeTo": ""}], "Data": [{"Day": "", "DayNumber": "", "Time": {"Time": "", "Code": "", "TimeFrom": "", "TimeTo": ""}, "Class": {"Code": "", "Name": "", "TeacherFull": "", "Teacher": "", "Form": ""}, "Group": {"Code": "", "Name": ""}, "Room": {"Code": "", "Name": ""}}], "Semestr": "Весенний семестр 2020-2021 г. "}

    for key_l1 in parsed_json.keys():
        if key_l1 in struct.keys():
            if key_l1 in ["Times", "Data"] and isinstance(parsed_json[key_l1], list):
                if list(parsed_json[key_l1][0].keys()).sort() == list(struct[key_l1][0].keys()).sort():
                    success.append("Структура расписания распознана")
                else:
                    errors.append("Ошибка проверки структуры расписания: в ключе {} ожидается структура {}".format(key_l1, " ,".join(list(struct[key_l1][0].keys()))))
            elif key_l1 == "Semestr":
                pass
            else:
                errors.append("Ошибка проверки структуры расписания: в ключе {} ожидается list".format(key_l1))

        else:
            errors.append("Ошибка проверки структуры расписания: не найден ключ {}".format(key_l1))

    return success, errors


def parse_schedule(json_file):
    errors = []
    success= []
    try:
        parsed_json = json.loads(json_file)
        success, errors = check_schedule_structure(parsed_json)
        if not errors:
            data_schedule = parsed_json["Data"]
            for item in data_schedule:
                day = item["Day"]

                day_number = item["DayNumber"]
                week_alt_obj = WeekAlternationList.objects.get(alternation_code=day_number)

                time_code = item["Time"]["Code"]
                time_obj = Times.objects.get(time_code=time_code)

                teacher_full_name = item["Class"]["TeacherFull"]
                teacher_name = item["Class"]["Teacher"]
                teacher_obj, created = Teacher.objects.get_or_create(teacher_full=teacher_full_name, teacher=teacher_name)

                class_code = item["Class"]["Code"]
                class_name = item["Class"]["Name"]
                class_form = item["Class"]["Form"]
                discipline_obj, created = Discipline.objects.get_or_create(code=class_code, name=class_name, form=class_form)

                room_code = item["Room"]["Code"]
                room_name = item["Room"]["Name"]
                room_obj, created = Room.objects.get_or_create(code=room_code, name=room_name)

                group_code = item["Group"]["Code"]
                group_name = item["Group"]["Name"]
                group_obj, created = Group.objects.get_or_create(code=group_code, name=group_name)

                schedule_obj, created = Schedule.objects.get_or_create(day=day,
                                                                       alternation_week=week_alt_obj,
                                                                       class_time=time_obj,
                                                                       group=group_obj,
                                                                       discipline=discipline_obj,
                                                                       teacher=teacher_obj,
                                                                       room=room_obj)

            success.append("Раcписание группы {} успешно загружено".format(group_name))

    except Exception as e:
        errors.append(e)

    return success, errors
