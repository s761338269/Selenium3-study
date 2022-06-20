# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :class_study.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 14:39
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# expected_conditions函数，一单出现这个元素就执行
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class GJsPoject:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def openbrower(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(2)

    def by_css(self, loc):
        """重写css定位"""
        return self.driver.find_element(By.CSS_SELECTOR, loc)

    def input_username(self,loc,text):
        self.by_css(loc).send_keys(text)

    def input_userpwd(self,loc,text):
        self.by_css(loc).send_keys(text)

    def click_login_btn(self, loc):
        self.by_css(loc).click()

    def assert_success_text(self,loc):
        element = WebDriverWait(self.driver, 3, 0.5).until(expected_conditions.presence_of_element_located(loc))
        return element.text

    def login_gjs(self,url,loc,username,loc1,password,loc2,loc3,exceptText,loc4,exceptText1):
        self.openbrower(url)
        sleep(1)
        self.input_username(loc,username)
        sleep(1)
        self.input_userpwd(loc1,password)
        sleep(1)
        self.click_login_btn(loc2)
        sleep(1)
        try:
            if self.assert_success_text(loc3) == exceptText: #登录成功
                print('pass')
            else:
                print(self.assert_success_text(loc3))
                print('false')
        except:
            if self.assert_success_text(loc4) == exceptText1: #密码错误
                print("手机号或密码错误")
            else:
                print(self.assert_success_text(loc4))
                print('false')
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    t = GJsPoject()
    url = 'https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com'
    loc = '#phone'
    loc1 = '#pwd'
    loc2 = '#loginBtn'
    loc3 = (By.CSS_SELECTOR,'#siteName')
    loc4 = (By.CSS_SELECTOR,'#err-txt')
    username = '17304165410'
    password = 'a7641345512'
    exceptText = '广州航海学院'
    exceptText1 = '手机号或密码错误'
    t.login_gjs(url,loc,username,loc1,password,loc2,loc3,exceptText,loc4,exceptText1)




