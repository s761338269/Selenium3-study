# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_Login.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 17:39

import unittest

from PO_study.common.getImage import SaveImage
from PO_study.common.helper import Helper
from PO_study.common.ownUnit import MyunitTests


class TestLogin(MyunitTests,Helper):

    def test_login(self):
        """正确的用户名和密码"""
        self.loginpage.openLoginPage()
        self.log('PO-xxt:打开浏览器进入学习通登录界面')
        self.loginpage.login_xxt_pro('1******0','a******9')
        self.log('PO-xxt:输入正确的账号密码')
        self.assertEqual(self.loginpage.get_assertText(),'广州航海学院')
        self.log('PO-xxt:登录成功获取信息进行断言')
        SaveImage(self.dr, 'login_success.png')
        self.log('PO-xxt:登录成功后获取截图信息')
    def test_user_null(self):
        """用户名为空"""
        self.loginpage.openLoginPage()
        self.log('PO-xxt:打开浏览器进入学习通登录界面')
        self.loginpage.login_xxt_pro('','a7*****269')
        self.log('PO-xxt:不输入账号，只输入密码')
        self.assertEqual(self.loginpage.userNull(),'请输入手机号')
        self.log('PO-xxt:获取登录失败信息进行断言')

    def test_psw_null(self):
        """密码为空"""
        self.loginpage.openLoginPage()
        self.log('PO-xxt:打开浏览器进入学习通登录界面')
        self.loginpage.login_xxt_pro('17******570', '')
        self.log('PO-xxt:不输入密码')
        self.assertEqual(self.loginpage.pswNull(), '请输入密码')
        self.log('PO-xxt:获取登录失败信息进行断言')
    def test_user_false(self):
        """账号密码错误"""
        self.loginpage.openLoginPage()
        self.log('PO-xxt:打开浏览器进入学习通登录界面')
        self.loginpage.login_xxt_pro('17******70', '123456')
        self.log('PO-xxt:输入错误的账号密码')
        self.assertEqual(self.loginpage.userFalse(), '手机号或密码错误')
        self.log('PO-xxt:获取登录失败信息进行断言')

if __name__ == '__main__':
    unittest.main(verbosity=2)