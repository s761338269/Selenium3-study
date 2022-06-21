# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_1.py
# @author   : 声培 
# @Time     : 2022/6/21 0021 1:35
import unittest
import sys


from common.ownUnit import MyunitTests


class TestLogin(MyunitTests):


    def test_1(self):
        print(1)

if __name__ == '__main__':
    unittest.main(verbosity=2)