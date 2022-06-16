# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :altert_study.py
# @author   : 声培 
# @Time     : 2022/6/16 0016 17:05

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

dr = webdriver.Firefox()
url = 'https://www.baidu.com'
dr.get(url)
sleep(1)
setting  = dr.find_element(By.ID,'s-usersetting-top')
ActionChains(dr).move_to_element(setting).perform()
dr.find_element(By.LINK_TEXT,'搜索设置').click()
sleep(1)
dr.find_element(By.CLASS_NAME,'pftab_hd').find_element(By.XPATH,"//li[@class='item']").click()
sleep(1)
dr.find_element(By.CLASS_NAME,'pftab_hd').find_element(By.XPATH,"//li[@class='item']").click()
# 搜索框输入提示设置不显示
sleep(1)
dr.find_element(By.ID,'s1_2').click()
sleep(1)
dr.find_element(By.LINK_TEXT,'保存设置').click()
sleep(2)
# 获取弹出的提示信息，日志输出
alert_text = dr.switch_to.alert.text
print(alert_text)
# 用于点击‘确定’按钮操作
# dr.switch_to.alert.accept()
# 拒绝警告框，相当于点取消
dr.switch_to.alert.dismiss()
dr.quit()



