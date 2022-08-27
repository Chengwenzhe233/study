# coding=utf-8
import unittest
import os
import HTMLTestRunner

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
        self.assertEqual(res["code"], 201)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LiankeyunCase("test_page"))
    report_path = os.path.dirname(os.getcwd()) + "/Report/report.html"
    with open(report_path, "wb")as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="cwz", description="cwz test")
        runner.run(suite)
    f.close()
    # unittest.main()
