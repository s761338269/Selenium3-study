# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_Login_ddt.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 20:54
import unittest

import ddt

from PO_study.common.ownUnit import MyunitTests


def readData():
    Data = [
        ['17******570','a*****69','广州航海学院'],
        ['', '123456', '请输入手机号'],
        ['1324564554', '', '请输入密码'],
        ['789456', 'asdsadasd', '手机号或密码错误']
    ]
    return Data
@ddt.ddt
class TestLogin(MyunitTests):
    @ddt.data(*readData())
    @ddt.unpack
    def test_login(self,username,password,expectText):
        self.loginpage.openLoginPage()
        self.loginpage.login_xxt_pro(username,password)
        try:
            self.assertEqual(self.loginpage.get_assertText(),expectText)
        except:
            try:
                if self.assertEqual(self.loginpage.userNull(),expectText):
                    print(expectText)
            except:
                try:
                    if self.assertEqual(self.loginpage.pswNull(),expectText):
                        print(expectText)
                except:
                    if self.assertEqual(self.loginpage.userFalse(),expectText):
                        print(expectText)
                    else:
                        print("发送页面发送未知错误")




if __name__ == '__main__':
    unittest.main(verbosity=2)