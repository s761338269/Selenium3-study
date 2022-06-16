# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :mouse_study.py
# @author   : 声培 
# @Time     : 2022/6/16 0016 11:14
from selenium import webdriver
from time import sleep
#导入ActionChains类
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

dr = webdriver.Firefox()
dr.get('http://www.baidu.com')
sleep(2)
# # 定位到需要悬停的元素
# setting = dr.find_element(By.ID,'s-usersetting-top')
# # move_to_elemnt悬停操作,perform()用于执行所有操作
# ActionChains(dr).move_to_element(setting).perform()
# sleep(1)
# # LINK_TEXT是必须用在<a></a>中的才行
# dr.find_element(By.LINK_TEXT,"搜索设置").click()

# # 鼠标右键操作
# context = dr.find_element(By.ID,'su')
# ActionChains(dr).context_click(context).perform()

#鼠标双击操作
dr.find_element(By.ID,'kw').send_keys('为什么要双击一下')
sleep(2)
double = dr.find_element(By.ID,'su')
ActionChains(dr).double_click(double).perform()

sleep(2)
dr.quit()