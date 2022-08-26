#coding=utf-8
import unittest
import mock
import requests


def post_requst(url, data):
    res = requests.post(url, data).json()
    return res


def get_requst(url, data):
    res = requests.get(url, data).json()
    return res


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case执行开始")

    def tearDown(self):
        print("case执行结束")

    def test_01(self):
        url = "https://www.baidu.com/"
        data = {
            "username": "chengwenzhe"
        }
        success_test = mock.Mock(return_value= data)
        post_requst = success_test
        res = post_requst
        self.assertEqual("123456789", res())


if __name__ == "__main__":
    unittest.main()
