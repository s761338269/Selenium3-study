# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :excel_ddt_stduy.py
# @author   : 声培 
# @Time     : 2022/6/19 0019 0:19
import unittest,xlrd,ddt
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



def readData():
    book = xlrd.open_workbook('data.xls','r')
    table = book.sheet_by_index(0)  #获取第一个sheet表
    newRows =[]
    # 从第二行开始遍历，每一行
    for rowValue in range(1,table.nrows):
        newRows.append(table.row_values(rowValue,0,table.ncols))
    return newRows
@ddt.ddt
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

    @ddt.data(*readData())
    @ddt.unpack
    def test_sohuLogin(self,user,password,text):
        self.dr.get(self.testUrl)
        sleep(2)
        # '.'代表class,‘#’代表id
        # 当类名中有空格，要用'.'代替空格，如'addFocus ipt-account ng-pristine ng-valid' 换成'addFocus.ipt-account.ng-pristine.ng-valid'
        self.by_css('.addFocus.ipt-account.ng-pristine.ng-valid').send_keys(user)
        self.by_css('.addFocus.ng-pristine.ng-valid').send_keys(password)
        self.by_css('.btn-login.fontFamily').click()
        self.assertEqual(self.getassertText(),text,'登录出现异常')



if __name__ == '__main__':
    unittest.main()


