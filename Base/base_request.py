# coding=utf-8
import json

import requests


class BaseRequest:
    """发送post请求"""

    def send_post(self, url, headers, data):
        res = requests.post(url=url, headers=headers, json=data).text
        return res

    """发送get请求"""

    def send_get(self, url, headers, data):
        res = requests.get(url=url, headers=headers, params=data).text
        return res

    """执行方法，传递method、url、data参数"""

    def run_main(self, method, url, headers, data):
        if method == "get":
            res = self.send_get(url, headers, data)
        else:
            res = self.send_post(url, headers, data)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        return res
