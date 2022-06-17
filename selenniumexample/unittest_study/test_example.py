# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_example.py
# @author   : 声培 
# @Time     : 2022/6/17 0017 19:19

import unittest
class Test(unittest.TestCase):
    def test_strendswitch(self):
        self.assertEqual('foo'.endswith('o'),True)

    def test_split(self):
        s = 'my happy days'
        self.assertEqual(s.split(),['my','happy','days'])

if __name__ == '__main__':
    unittest.main()