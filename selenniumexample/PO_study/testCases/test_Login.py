# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_Login.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 17:39

import unittest

from PO_study.common.ownUnit import MyunitTests


class TestLogin(MyunitTests):

    def test_login(self):
        """正确的用户名和密码"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro('17*******70','a7******9')
        self.assertEqual(self.loginpage.get_assertText(),'广州航海学院')
    def test_user_null(self):
        """用户名为空"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro('','a7*****269')
        self.assertEqual(self.loginpage.userNull(),'请输入手机号')

    def test_psw_null(self):
        """密码为空"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro('17******570', '')
        self.assertEqual(self.loginpage.pswNull(), '请输入密码')
    def test_user_false(self):
        """账号密码错误"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro('17******70', '123456')
        self.assertEqual(self.loginpage.userFalse(), '手机号或密码错误')

if __name__ == '__main__':
    unittest.main(verbosity=2)