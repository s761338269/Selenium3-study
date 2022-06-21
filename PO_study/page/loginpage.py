# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :loginpage.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 16:43
from time import sleep

from selenium.webdriver.common.by import By

from basepase.homeBase import HomePage

class LoginPage(HomePage):
    #定位器
    #用户名
    username_loc = (By.ID,'phone')
    #密码
    psw_loc = (By.ID,'pwd')
    #登录按钮
    btn_loc = (By.ID,'loginBtn')
    #获取登录成功后的信息
    loginBtn_loc = (By.ID,'siteName')
    #用户名为空
    userNull_loc = (By.ID,'phoneMsg')
    #密码为空
    pswNull_loc = (By.ID,'pwdMsg')
    #账号密码错误
    userFalse_loc = (By.ID,'err-txt')

    # 打开登录界面
    def openLoginPage(self):
        self.dr.get(self.url)
        self.dr.maximize_window()
        self.dr.refresh()
        sleep(0.5)

    #输入用户名
    def input_useName(self,userName):
        self.find_element(*self.username_loc).send_keys(userName)

    #输入密码
    def input_usePsw(self,pswName):
        self.find_element(*self.psw_loc).send_keys(pswName)
    #单击登录
    def btn_login(self):
        self.find_element(*self.btn_loc).click()
    #获取登录后的提示信息
    def get_assertText(self):
        return self.find_element(*self.loginBtn_loc).text
    #获取用户名为空的提示
    def userNull(self):
        return self.find_element(*self.userNull_loc).text
    #获取密码为空的登录信息
    def pswNull(self):
        return self.find_element(*self.pswNull_loc).text
    #获取账号或密码错误的信息
    def userFalse(self):
        return self.find_element(*self.userFalse_loc).text

    #封装成登录流程
    def login_xxt_pro(self,username,password):
        self.input_useName(username)
        self.input_usePsw(password)
        self.btn_login()
        sleep(1)