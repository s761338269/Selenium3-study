# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :JavaScript_study.py
# @author   : 声培 
# @Time     : 2022/6/16 0016 17:00
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# JavaScript处理富文本
# 本次因为没有搭建网址，并没有成功。
# dr = webdriver.Firefox()
# dr.get('http://localhost:8080')
# js = "document.getElementById('content_ifr;).contentWindow.document.body.innerHTML='%s'" %(A)
# dr.execute_script(js)

# 处理隐藏元素实战
dr = webdriver.Firefox()
dr.get(r'D:\python_work\xialakuang.html')
sleep(1)
# 将隐藏改为可见
js = 'document.querySelectorAll("select")[0].style.display="block";'
dr.execute_script(js)
sleep(3)
element = dr.find_element(By.ID,'s1Id')
# 选择显示那个下拉选项
Select(element).select_by_visible_text("o2")

