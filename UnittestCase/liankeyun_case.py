# coding=utf-8
import unittest
from Base import base_request

host = "https://work.liankeyun.com/"


class LiankeyunCase(unittest.TestCase):
    def test_page(self):
        url = host + "wsg/dataCenter/weChat/operation/page"
        headers = {
            "Authorization": "eyJhbGciOiJIUzUxMiJ9"
                             ".eyJsb2dpbl91c2VyX2tleSI6ImMwYWExM2ZiLTEwY2EtNGNiYy1iMjg4LWM1ZDAzOTJhYjE4ZSJ9"
                             ".AdKTmyqJ3SBf3BihbfnzfUk92guiegcE3A_hsnmf6ZOkSH2NGoDhWIUj9J4UU4vAJm3wK2NTvYoX-VG9D-4Fkg ",
            "content-type": "application/json"
        }
        data = {
            "page": 1,
            "size": 3,
            "query": {}
        }
        request = base_request.BaseRequest()
        res = request.run_main("post", url, headers, data)
        # print(type(res))
        self.assertEqual(res["code"], 200)


if __name__ == "__main__":
    unittest.main()
