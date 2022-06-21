# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :nohead_study.py
# @author   : 声培 
# @Time     : 2022/6/21 0021 20:09
from selenium import webdriver
#创建新实例
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service

# options = webdriver.FirefoxOptions()
# #设置Firefox 无头模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# s =Service(r'D:\Python37\geckodriver.exe')
# # executable_path = r'D:\Python37\geckodriver.exe'    #方法太旧，已弃用火狐浏览器驱动所在路径
# driver = webdriver.Firefox(options=options,service=s)
# driver.get("https://www.baidu.com")
# driver.close()


#创建新实例
chrome_options =Options()
#设置Chrome无头模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.baidu.com")
print("好了")
driver.close()