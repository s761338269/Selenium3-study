# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :find_element.py
# @author   : 声培 
# @Time     : 2022/6/14 0014 23:46

from time import sleep

import dr as dr
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
sleep(1)
driver.get('http://www.baidu.com')
sleep(1)

# #使用元素id定位
# driver.find_element(By.ID,"kw").send_keys("你好")

# #使用元素name定位
# driver.find_element(By.NAME,"wd").send_keys("你好")

# # 使用元素class_name定位,但尽量不要用class去定位，因为class不唯一
# driver.find_element(By.CLASS_NAME, 's_ipt') .send_keys("你好")

# #通过xpath定位元素,//代表相对路径，通过相对路径找到对应的元素。
# driver.find_element(By.XPATH,"//input[@id='kw']").send_keys('早上好')

# #通过父级相对路径找到对应的元素。
# driver.find_element(By.XPATH,"//form[@id='form']/span/input").send_keys('早上好')

# #通过两个标注增强标签的唯一性
# driver.find_element(By.XPATH,"//input[@id='kw' and @class='s_ipt']").send_keys('早上好')

# #通过css_select来定位，’#‘代表id,class用'.'来表示,
# '>'代表层级关系，如form>input，form是input的父级。为了简洁’>'可以省略，用‘ ’ 代替
# driver.find_element(By.CSS_SELECTOR,"input#kw").send_keys('早上好')
driver.find_element(By.CSS_SELECTOR,"input.s_ipt").send_keys('早上好')
# driver.find_element(By.CSS_SELECTOR,"form#form>span>input").send_keys('早上好')

# 存在多标签时的操作,for循环筛选定位
# tag = driver.find_elements(by=By.TAG_NAME,value='input')
# for t in tag:
#     if t.get_attribute('autocomplete') == 'off':
#         t.send_keys('fighter007')
#         sleep(2)
#         driver.find_element(By.ID,'su').click()
#         sleep(2)
#         driver.quit()
sleep(2)
driver.quit()