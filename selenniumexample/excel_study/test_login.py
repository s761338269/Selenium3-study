# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_login.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 21:41

import unittest,xlrd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



def readUsername(row):
    '''读取用户名'''
    book = xlrd.open_workbook('data.xls','r')
    table = book.sheet_by_index(0)  #获取第一个sheet表
    # 获取第一列的所有数据
    return table.row_values(row)[0]

def readPassword(row):
    '''读取密码'''
    book = xlrd.open_workbook('data.xls', 'r')
    table = book.sheet_by_index(0)  # 获取第一个sheet表
    # 获取第一列的所有数据
    return table.row_values(row)[1]

def readAssertText(row):
    '''读取预期结果'''
    book = xlrd.open_workbook('data.xls', 'r')
    table = book.sheet_by_index(0)  # 获取第一个sheet表
    # 获取row行第一列的数据
    return table.row_values(row)[2]

class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.dr = webdriver.Firefox()
        self.testUrl = 'https://mail.sohu.com/fe/#/login'

    def tearDown(self) -> None:
        self.dr.quit()

    def by_css(self,usernameloc):
        """重写css定位"""
        return self.dr.find_element(By.CSS_SELECTOR,usernameloc)

    def getassertText(self):
        """获取验证信息"""
        try:
            sleep(2)
            loctor = (By.CSS_SELECTOR,'.tipHolder.ng-binding')
            WebDriverWait(self.dr,5,0.5).until(expected_conditions.presence_of_element_located(loctor))
            return self.by_css('.tipHolder.ng-binding').text
        except Exception as message:
            print('元素定位报错，报错原因是：{}'.format(message))

    def souhuLogin(self,user,password):
        '''封装登录功能'''
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(password)
        self.by_css('.btn-login.fontFamily').click()

    def test_souhuLogin_001(self):
        '''账号密码都输入但是错误'''
        self.dr.get(self.testUrl)
        sleep(3)
        self.souhuLogin(readUsername(1),readPassword(1))
        self.assertEqual(self.getassertText(),readAssertText(1))

    def test_souhuLogin_002(self):
        '''账号为空'''
        self.dr.get(self.testUrl)
        sleep(3)
        self.souhuLogin(readUsername(2),readPassword(2))
        self.assertEqual(self.getassertText(),readAssertText(3))
    def test_souhuLogin_003(self):
        '''账号密码密码为空'''
        self.dr.get(self.testUrl)
        sleep(3)
        self.souhuLogin(readUsername(3),readPassword(3))
        self.assertEqual(self.getassertText(),readAssertText(3))
    def test_souhuLogin_004(self):
        '''密码为空'''
        self.dr.get(self.testUrl)
        sleep(3)
        self.souhuLogin(readUsername(4),readPassword(4))
        self.assertEqual(self.getassertText(),readAssertText(4))





if __name__ == '__main__':
    unittest.main()


