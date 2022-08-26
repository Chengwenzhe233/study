#coding=utf-8
import unittest
import os
# from UnittestCase.test_case01 import TestCase01
# from UnittestCase.test_case02 import TestCase02
# from UnittestCase.test_case03 import TestCase03
#
# case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
# suite = unittest.TestSuite([case_01, case_02, case_03])
# runner = unittest.TextTestRunner()
# runner.run(suite)
case_path = os.getcwd()
discover = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)
