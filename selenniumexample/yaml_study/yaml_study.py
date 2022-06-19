# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :yaml_study.py
# @author   : 声培 
# @Time     : 2022/6/19 0019 13:52


from time import sleep
import yaml,unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def readYaml():
    """获取所有YAML数据"""
    f = open('data.yaml','r',encoding='utf-8')
    # yaml.load()用于读取data.yaml文件的所有文件
    # 转换成Python对象
    data = yaml.safe_load(f)
    f.close()
    return data

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
        self.souhuLogin(readYaml()['userNull']['username'],readYaml()['userNull']['password'])
        self.assertEqual(self.getassertText(),readYaml()['userNull']['assertText'])

    def test_souhuLogin_002(self):
        '''账号为空'''
        self.dr.get(self.testUrl)
        sleep(3)
        self.souhuLogin(readYaml()['userPass']['username'], readYaml()['userPass']['password'])
        self.assertEqual(self.getassertText(), readYaml()['userPass']['assertText'])

    def test_souhuLogin_003(self):
        '''账号密码错误'''
        self.dr.get(self.testUrl)
        sleep(3)
        self.souhuLogin(readYaml()['userFlase']['username'], readYaml()['userFlase']['password'])
        self.assertEqual(self.getassertText(), readYaml()['userFlase']['assertText'])






if __name__ == '__main__':
    unittest.main()