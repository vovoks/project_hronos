import unittest

from main import *


class TestScheduleParser(unittest.TestCase):

    def test_request_handler_success(self):
        url = "https://miet.ru/schedule" + "/groups"
        data = {}
        result, errors = request_handler(url, data)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()