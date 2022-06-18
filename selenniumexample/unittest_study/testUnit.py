# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :testUnit.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 11:12


# TestModle()测试类继承TestWebUI()类
from unittest_study.Myunit import TestWebUI


class TestModle(TestWebUI):
    def test_QQlogin(self):
        self.dr.get('https://mail.qq.com')
        self.assertEqual(self.dr.title, '登录QQ邮箱', '跳转登录页面失败')

    def test_WBlogin(self):
        self.dr.get('https://www.maoyan.com/')
        self.assertEqual(self.dr.title, '猫眼电影 - 娱乐看猫眼', '页面跳转失败')
