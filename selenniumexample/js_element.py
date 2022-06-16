# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :js_element.py
# @author   : 声培 
# @Time     : 2022/6/15 0015 11:14

# JavaScript定位的方式有，getElementsByClassName()、getElementById()、getElementsByName()、getElementsByTagName()
# 和document.querySelectorAll()
# 除了getElementById定位是返回单个element元素定位以外，其他定位方式都是返回list对象。

from selenium import webdriver
import  time as t
dr = webdriver.Chrome()
dr.get('http://www.jianshu.com/sign_in')
t.sleep(2)
# #单击“注册”按钮
# js_register = 'document.getElementById("js-sign-up-btn").click();'
# dr.execute_script(js_register)  #execute_script()用于执行javaScript脚本
# t.sleep(2)

#单击”登录“按钮
js_class = 'document.getElementsByClassName("active")[0].click();'
dr.execute_script(js_class)
t.sleep(2)

# 输入账户密码,通过网页发现,登录的input是第三个，密码是第四个input
#输入xiaochen
js_user = 'document.getElementsByTagName("input")[2].value="xiaochen";'
dr.execute_script(js_user)
t.sleep(2)
# 密码传入123456
js_password = 'document.getElementsByTagName("input")[3].value="123456";'
dr.execute_script(js_password)
t.sleep(2)

# 使用css选择器定位"登录"按钮, '#'代表选择定位元素id，当然id是唯一的,'.'选择定位元素class
# css_btn = 'document.querySelectorAll("#sign-in-form-submit-btn")[0].click();'
css_btn = 'document.querySelectorAll(".sign-in-button")[0].click();'
dr.execute_script(css_btn)
