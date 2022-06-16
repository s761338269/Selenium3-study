# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :window_study.py
# @author   : 声培 
# @Time     : 2022/6/16 0016 13:04
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

# 窗口切换实战

# 方法一：Get方法
# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
# driver.find_element(By.ID,'kw').send_keys('百度贴吧')
# driver.find_element(By.ID,'su').click()
# #第一个窗口下单机‘百度贴吧’这个链接
# sleep(2)
# driver.find_element(By.XPATH,'//*[@id="2"]/div/h3/a').click()
# # Get方法实战
# driver.get('https://tieba.baidu.com/f?kw=%CC%F9%B0%C9&fr=ala0&tpl=5&dyTabStr=MCw2LDQsMywxLDUsMiw3LDgsOQ%3D%3D')
# sleep(3)
# driver.find_element(By.LINK_TEXT,'进入贴吧').click()
# driver.quit()


# 方法2：使用Switch方法切换窗口
driver = webdriver.Firefox()
url = 'http://www.so.com'
driver.get(url)
sleep(1)
driver.find_element(By.LINK_TEXT,'360导航').click()
sleep(2)
# 获取当前窗口数
windows = driver.window_handles
# 选择第二个窗口
driver.switch_to.window(windows[1])
sleep(1)
driver.find_element(By.ID,'search-kw').send_keys("第二个窗口")
driver.find_element(By.ID,'search-btn').click()
sleep(2)
windows = driver.window_handles
# 返回第一个窗口
driver.switch_to.window(windows[0])
sleep(2)
# 返回第三个窗口
driver.switch_to.window(windows[2])
sleep(2)
driver.quit()