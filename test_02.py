#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/20 9:29 
# @Author : TETE
# @File : test_02.py
import unittest
class Test02(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("这是setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是tearDownClass")


    def test02_demo01(self):
        print("test02_demo01")
        self.assertEqual(1, 2, "判断相等")

    def test02_demo02(self):
        print("执行test02_demo02")
        self.assertEqual(2, 2, "判断相等")

    # @unittest.skipIf(1 + 1 == 2, "跳过这条用例")
    def test02_demo03(self):
        print("执行test02_demo03")
        self.assertIn('h', 'hello')

