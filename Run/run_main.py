# coding=utf-8
import os
import unittest
import json
from Util.handle_excel import HandleExcel
from Util.handle_init import HandleInit
from Base.base_request import BaseRequest


class RunMain:
    def run_case(self):
        excel_data = HandleExcel()
        request = BaseRequest()
        ini_data = HandleInit()
        host = ini_data.get_value(section="server", key="host")
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i + 2)
            is_run = data[2]
            if is_run == "yes":
                method = data[6]
                url = host + data[5]
                header = json.loads(data[9])
                data1 = json.loads(data[7])
                # request.run_main(method=method, url=url, headers=header, data=data1)
                print(request.run_main(method=method, url=url, headers=header, data=data1))


if __name__ == "__main__":
    RunMain().run_case()
