# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :homeBase.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 16:37
from selenium.webdriver.support.wait import WebDriverWait
# expected_conditions函数，一单出现这个元素就执行
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self,url,dr):  #定义驱动和地址url
        self.url = url
        self.dr = dr

    def find_element(self,*loc):    #封装元素定位方式
        try:
            WebDriverWait(self.dr,20).until(EC.presence_of_element_located(loc))
            return self.dr.find_element(*loc)
        except:
            print(*loc + '当前页面没找到该元素！')



