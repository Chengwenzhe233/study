#coding=utf-8
import requests
import unittest


class TestCase03(unittest.TestCase):
    def setUp(self):
        print("开始执行")

    def tearDown(self):
        print("执行结束")

    @classmethod
    def setUpClass(cls):
        print("case开始执行")

    @classmethod
    def tearDownClass(cls):
        print("case执行结束")

    def test_03(self):
        print("test03")

    def test_02(self):
        print("test02")

    def test_01(self):
        print("test01")


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(TestCase01("test_02"))
    tests = [TestCase03("test_02"), TestCase03("test_01")]
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
