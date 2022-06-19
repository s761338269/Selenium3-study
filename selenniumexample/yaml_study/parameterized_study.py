# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :parameterized_study.py
# @author   : 声培 
# @Time     : 2022/6/19 0019 14:40
import unittest,xlrd
from time import sleep

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class LoginTest(unittest.TestCase):

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

    def souhuLogin(self,username,password):
        '''封装登录功能'''
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(username)
        sleep(0.5)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(password)
        self.by_css('.btn-login.fontFamily').click()

# 例子失败
#     因为@parameterized.expand(c)参数化3个参数，name,input,expected,3组参数。传入测试方法名字和具体数值
#     name是属性值,input才是输入的值，name不能为空的。
    @parameterized.expand([
        ('','','请输入账号密码'),
        ('admin233213@sohu', '', '请输入账号密码'),
        ('admin233213@sohu', '1234556', '请输入正确的账号密码'),
        ('', '7613382', '请输入账号密码')
    ])
    def test_login(self,username,password,assert_text):
        self.dr.get(self.testUrl)
        sleep(3)
        self.souhuLogin(username,password)
        self.assertEqual(self.getassertText(),assert_text,'登录异常')
        sleep(0.5)

if __name__ == '__main__':
    unittest.main()