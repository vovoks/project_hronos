import json

import requests
import logging
BASE_URL = "https://miet.ru/schedule"

from time import sleep

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def request_handler(url, data, request_type='post'):
    errors = []
    result = ""
    if request_type == 'post':
        r = requests.post(url, data)
        if r.status_code == 200:
            result = json.loads(r.text)
        else:
            errors.append("Request code: {}, request data: {}".format(r.status_code, r.text))
    else:
        errors.append('Unsupported request type: {}'.format(request_type))
    return result, errors


def get_groups():
    url = BASE_URL + "/groups"
    data = {}
    return request_handler(url, data)


def get_schedule(group_name: str):
    url = BASE_URL + "/data"
    data = {"group": group_name}
    return request_handler(url, data)


def parse_schedule():
    logging.info("===GET SCHEDULE===")
    schedule = {}
    logging.info("get_groups")
    group_list, errors = get_groups()
    if errors:
        [logging.error(x) for x in errors]

    for group in group_list[:3]:
        sleep(0.3)
        logging.info("get_group: {}".format(group))
        schedule[group], errors = get_schedule(group)
        with open("schedules/{}.json".format(group), "w+", encoding='utf8') as f:
            f.write(json.dumps(schedule, ensure_ascii=False))
        if errors:
            [logging.error(x) for x in errors]


if __name__ == '__main__':
    parse_schedule()