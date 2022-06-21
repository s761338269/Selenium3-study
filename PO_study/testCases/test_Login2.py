# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_Login2.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 20:37

import unittest

from common.getImage import SaveImage
from common.helper import Helper
from common.ownUnit import MyunitTests


class TestLogin(MyunitTests,Helper):

    def test_login(self):
        """正确的用户名和密码"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro(self.readusername(1),self.readuserpsd(1))
        try:
            self.assertEqual(self.loginpage.get_assertText(),self.exceptText(1))
            SaveImage(self.dr,'login_success.png')
        except:
            # 如果用例失败请截图
            SaveImage(self.dr, 'login_success1.png')
    def test_user_null(self):
        """用户名为空"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro(self.readusername(2), self.readuserpsd(2))

        self.assertEqual(self.loginpage.userNull(), self.exceptText(2))
        SaveImage(self.dr, 'loginuserNull.png')
    def test_psw_null(self):
        """密码为空"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro(self.readusername(3), self.readuserpsd(3))
        self.assertEqual(self.loginpage.pswNull(), self.exceptText(3))
        SaveImage(self.dr, 'loginpswNull.png')
    def test_user_false(self):
        """账号密码错误"""
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro(self.readusername(4), self.readuserpsd(4))
        self.assertEqual(self.loginpage.userFalse(), self.exceptText(4))
        SaveImage(self.dr, 'loginflase.png')

if __name__ == '__main__':
    unittest.main(verbosity=2)