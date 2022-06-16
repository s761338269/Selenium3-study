# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :form_study.py
# @author   : 声培 
# @Time     : 2022/6/16 0016 12:07
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://mail.qq.com/cgi-bin/loginpage')
sleep(2)
# 当页面是用了iframe嵌套了其他页面，先进入对应的iframe
driver.switch_to.frame('login_frame')
driver.find_element(By.ID,'u').send_keys('761338269')
sleep(2)
driver.find_element(By.ID,'p').send_keys('123456789')
sleep(2)
driver.find_element(By.ID,'login_button').click()
driver.switch_to.default_content()
sleep(2)
driver.quit()

# 如遇到iframe的标签不止一个，
# 如嵌套的iframe，假设是login_frame1最外，login_frame2在login_frame1的里面
# 先进login_frame1
driver.switch_to.frame('login_frame1')
# 再进login_frame2
driver.switch_to.frame('login_frame2')
# 再进行定位等操作，如输入用户名
driver.find_element(By.ID,'u').send_keys('761338269')

# 平行表单切换，如进入iframe1,那么就要先退出iframe1，再进入iframe2
# 先进login_frame1
driver.switch_to.frame('login_frame1')
#退出login_frame1
driver.switch_to.default_content() #无论进入了几层iframe1，执行一次就退出到最外层。
# 再进login_frame2
driver.switch_to.frame('login_frame2')
# 再进行定位等操作，如输入用户名
driver.find_element(By.ID,'u').send_keys('761338269')

# 表单特殊处理
# 如遇到iframe的id和name，是随机生成的，或者没有id和那么，可以用层级定位xpath定位到iframe，然后再用driver.switch_to.driver.switch_to.frame(xpath)