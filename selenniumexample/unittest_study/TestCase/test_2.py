# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_2.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 11:36

from unittest_study.TestCase.Myunit import TestWebUI
# TestModle()测试类继承TestWebUI()类
class TestModle(TestWebUI):
    def test_QQlogin(self):
        """进入QQ邮箱登录界面"""
        self.dr.get('https://mail.qq.com')
        self.assertEqual(self.dr.title, '登录QQ邮箱', '跳转登录页面失败')

    def test_WBlogin(self):
        """进入猫眼电影首页"""
        self.dr.get('https://www.maoyan.com/')
        self.assertEqual(self.dr.title, '猫眼电影 - 娱乐看猫眼', '页面跳转失败')