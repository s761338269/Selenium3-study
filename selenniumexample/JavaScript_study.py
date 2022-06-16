# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :JavaScript_study.py
# @author   : 声培 
# @Time     : 2022/6/16 0016 17:00
from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# JavaScript处理富文本
# 本次因为没有搭建网址，并没有成功。
# dr = webdriver.Firefox()
# dr.get('http://localhost:8080')
# js = "document.getElementById('content_ifr;).contentWindow.document.body.innerHTML='%s'" %(A)
# dr.execute_script(js)

# # JS处理隐藏元素实战
# dr = webdriver.Firefox()
# dr.get(r'D:\python_work\xialakuang.html')
# sleep(1)
# # 将隐藏改为可见
# js = 'document.querySelectorAll("select")[0].style.display="block";'
# dr.execute_script(js)
# sleep(3)
# element = dr.find_element(By.ID,'s1Id')
# # 选择显示那个下拉选项
# Select(element).select_by_visible_text("o2")

# JS处理readonly、disable属性实战。
#
# # 利用removeAttribute去除无法输入。
# # 当我们发现，有个部分输入框input，无法修改时，可看看是否有readonly属性,可以利用js中的属性去移除readonly的属性。
# # 例如之前12306的官网的出发日期有时候是无法修改的，'https://kyfw.12306.cn/otn/leftTicket/init'，input里面的元素有readonly='readonly'属性。
# # 现在是返程日期不可以输入，可以通过js进行修改然后输入日期。
# dr = webdriver.Firefox()
# dr.get('https://kyfw.12306.cn/otn/leftTicket/init')
# sleep(2)
# # 通过removeAttribute()即可移除。移除返程日期里的disable。
# js1 = "document.getElementById('back_train_date').removeAttribute('disabled');"
# dr.execute_script(js1)
# sleep(2)
# dr.find_element(By.ID,'back_train_date').clear()
# sleep(2)
# dr.find_element(By.ID,'back_train_date').send_keys('2022-06-20')
# sleep(2)
# dr.quit()

# # JS处理浏览器滚动条实战
# # 当我们要定位的元素超出了我们的页面，就无法找到，所以要通过滑动滚动条
# dr = webdriver.Firefox()
# dr.get("http://www.baidu.com")
# dr.find_element(By.ID,'kw').send_keys("x8沙箱")
# dr.find_element(By.ID,'su').click()
# sleep(3)
# # 利用window.scrollTo(x,y)。x,y是以像素为单位的。x代表水平滚动栏的位置，y代表垂直的滚动栏的位置
# dr.execute_script("window.scrollTo(0,10000);")
# sleep(3)
# dr.execute_script("window.scrollTo(0,0);")
# sleep(3)
# dr.quit()

# 也可以用Key类下的DOWN、UP方法上下滑动
dr = webdriver.Firefox()
dr.get("http://www.baidu.com")
dr.find_element(By.ID,'kw').send_keys("x8沙箱")
dr.find_element(By.ID,'su').click()
sleep(3)
# 定位底部的‘下一页’的位置，来到页面底部
dr.find_element(By.XPATH,'//*[@id="page"]/div/a[10]').send_keys(Keys.DOWN)
sleep(3)
# 定位顶部的‘更多’的位置，返回顶部
dr.find_element(By.XPATH,'//*[@id="s_tab"]/div/a[9]').send_keys(Keys.UP)
sleep(3)
dr.quit()