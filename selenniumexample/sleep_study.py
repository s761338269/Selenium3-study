# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :sleep_study.py
# @author   : 声培 
# @Time     : 2022/6/16 0016 11:42
#鼠标双击操作

from selenium import webdriver
from time import sleep
#导入ActionChains类
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# dr = webdriver.Firefox()
# dr.get('http://www.baidu.com')
# # 隐式等待，内容还没加载出来，设置等待多久，如果内容出来就继续下一步
# dr.implicitly_wait(5)
# dr.find_element(By.ID,'kw').send_keys('为什么要双击一下')
# # 强制等待，强制等待你设置的时间
# sleep(2)
# double = dr.find_element(By.ID,'su')
# ActionChains(dr).double_click(double).perform()
# sleep(2)
# dr.quit()

#显示等待，WebDriverWait().until,在规定时间不断找寻需要定位的元素。
dr = webdriver.Chrome()
dr.get('https://mail.sina.com.cn/')
# presence_of_element_located表示只要有一个符合条件的元素加载出来就通过
element = WebDriverWait(dr,5,0.5).until(EC.presence_of_element_located((By.ID,'freename')))
element.send_keys('hello')

sleep(2)
dr.quit()