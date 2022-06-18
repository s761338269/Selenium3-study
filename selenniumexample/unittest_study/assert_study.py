# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :assert_study.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 0:00
import unittest
from selenium import webdriver
from time import sleep

class Test(unittest.TestCase):
    # 在测试类中，只在开始时执行一次
    @classmethod
    def setUpClass(cls) -> None:
        cls.dr = webdriver.Firefox()
    # 在测试类中，每个方法执行前执行一次
    # def setUp(self) -> None:
    #     self.dr = webdriver.Firefox()
    # 在测试类中，每个方法结束后执行一次
    # def tearDown(self) -> None:
    #     self.dr.quit()
    # 在测试类中，只在结束时执行一次
    @classmethod
    def tearDownClass(cls) -> None:
        cls.dr.quit()

    def test_QQlogin(self):
        self.dr.get('https://mail.qq.com')
        self.assertEqual(self.dr.title,'登录QQ邮箱','跳转登录页面失败')

    def test_WBlogin(self):
        self.dr.get('https://www.maoyan.com/')
        self.assertEqual(self.dr.title,'猫眼电影 - 娱乐看猫眼','页面跳转失败')

if __name__ == '__main__':
    unittest.main()

