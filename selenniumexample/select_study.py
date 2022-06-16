# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :select_study.py
# @author   : 声培 
# @Time     : 2022/6/15 0015 13:53
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
url = dr.get(r"file:\\D:\python_work\xialakuang.html")  #r是转义字符，说明后面的\是普通字符
element = dr.find_element(By.ID,"s1Id")
# 利用select类下拉选择，根据value定位,select_by.value
# Select(element).select_by_value('o2')

# 根据index索引来定位,索引从0开始的，0代表第一个。
# Select(element).select_by_index(0)

# 根据visible_text元素本身的文本描述来定位
# Select(element).select_by_visible_text('o3')

#也可以根据二次定位,但是要增加click事件
dr.find_element(By.ID,'s1Id').find_element(By.XPATH,"//*[@id='id3']").click()
sleep(5)