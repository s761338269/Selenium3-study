# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :ownUnit.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 18:45

import unittest
from time import sleep
from selenium import webdriver
from page.loginpage import LoginPage
# 分离测试固件
class MyunitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com'
        self.dr = webdriver.Firefox()
        self.dr.implicitly_wait(30)
        # 实例化一个loginpage对象
        self.loginpage = LoginPage(self.url, self.dr)

    def tearDown(self) -> None:
        self.dr.quit()