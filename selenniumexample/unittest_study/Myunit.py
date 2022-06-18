# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :Myunit.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 11:09
import unittest
from time import sleep

from selenium import webdriver

class TestWebUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.dr = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(1)
        cls.dr.quit()
