# coding=utf-8
import os
import unittest
from Util.handle_excel import HandleExcel


class RunMain:
    def run_case(self):
        excel_data = HandleExcel()
        rows = excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i + 1)
            print(data)


if __name__ == "__main__":
    RunMain().run_case()
