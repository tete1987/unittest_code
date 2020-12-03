#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/19 13:48 
# @Author : TETE
# @File : test_pytest01.py
import datetime
import os
import unittest
import HTMLTestRunner
import time

# class Demo(unittest.TestCase):
#     def setUp(self) -> None:
#         print("开始")
#
#     def tearDown(self) -> None:
#         print("结束")
#
#     def test_demo01(self):
#         print("test_demo01")
#         self.assertEqual(1,2,"判断相等")
#
# if __name__ == '__main__':
#     unittest.main()

# 2.setUp和tearDown会在没条测试用例执行完都执行，因此可加入setUpClass，在class中所有方法执行时只执行一次

# class Demo(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("这是setUpClass")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("这是tearDownClass")
#
#     def setUp(self) -> None:
#         print("开始")
#
#     def tearDown(self) -> None:
#         print("结束")
#
#     def test_demo01(self):
#         print("test_demo01")
#         self.assertEqual(1,2,"判断相等")
#
#     def test_demo02(self):
#         print("test_demo02")
#         self.assertEqual(2,2,"判断相等")
#
# if __name__ == '__main__':
#     unittest.main()


# 3.跳过某个用例
# class Demo(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("这是setUpClass")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("这是tearDownClass")
#
#     def setUp(self) -> None:
#         print("开始")
#
#     def tearDown(self) -> None:
#         print("结束")
#
#     def test_demo01(self):
#         print("test_demo01")
#         self.assertEqual(1,2,"判断相等")
#
#     def test_demo02(self):
#         print("test_demo02")
#         self.assertEqual(2,2,"判断相等")
#
#     @unittest.skipIf(1+1==2,"跳过这条用例")
#     def test_demo03(self):
#         print("test_demo03")
#         self.assertIn('h', 'hello')
#
# if __name__ == '__main__':
#     unittest.main()

# 4.加入测试套件


class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("这是setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是tearDownClass")

    # def setUp(self) -> None:
    #     print("开始")
    #
    # def tearDown(self) -> None:
    #     print("结束")

    def test_demo01(self):
        print("test_demo01")
        self.assertEqual(1, 2, "判断相等")

    def test_demo02(self):
        print("执行test_demo02")
        self.assertEqual(2, 2, "判断相等")

    # @unittest.skipIf(1 + 1 == 2, "跳过这条用例")
    def test_demo03(self):
        print("执行test_demo03")
        self.assertIn('h', 'hello')


class Demo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("这是Demo2 的 setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是Demo2 的tearDownClass")

    def test_Demo2_case1(self):
        print("执行test_Demo2_case1")
        self.assertIn('h', 'hello')


class HTMLTestRunnerNew(object):
    pass


if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # suit.addTest(Demo("test_demo03"))
    # suit.addTest(Demo2("test_Demo2_case1"))
    # unittest.TextTestRunner().run(suit)
    #执行某几个类的方法：
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo2)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner().run(suite)

    # now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # report_path = "D:\\python\\unittest_code"
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=(report_path, "wb"),
    #     title=u"页面报告",
    #     description=u"测试结果"
    # )
    discover = unittest.defaultTestLoader.discover("./", "test_case*.py")
    # unittest.TextTestRunner().run(discover)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = '/unittest_code\\report.html'
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例执行情况：')
    # unittest.TextTestRunner().run(discover)
    runner.run(discover)
    fp.close()