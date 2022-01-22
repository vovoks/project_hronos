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
