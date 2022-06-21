# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :nohead_study.py
# @author   : 声培 
# @Time     : 2022/6/21 0021 20:09
import threading
from time import sleep

from selenium import webdriver
#创建新实例
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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


# #创建新实例
# chrome_options =Options()
# #设置Chrome无头模式
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.baidu.com")
# print("好了")
# driver.close()

def baidu_search(browser,url):
    if browser == "FireFox":
        options = webdriver.FirefoxOptions()
        #设置Firefox 无头模式
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        s =Service(r'D:\Python37\geckodriver.exe')
        # executable_path = r'D:\Python37\geckodriver.exe'    #方法太旧，已弃用火狐浏览器驱动所在路径,用Service（）
        driver = webdriver.Firefox(options=options,service=s)

    elif browser == "Chrome":
        #创建新实例
        chrome_options =Options()
        #设置Chrome无头模式
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    sleep(3)
    driver.find_element(By.ID,'kw').send_keys(u"多线程启动不同浏览器")
    driver.find_element(By.ID,'su').click()
    print("搞定")
    sleep(3)
    driver.quit()

if __name__ == '__main__':
    data = {
        "FireFox" : 'http://www.baidu.com',
        "Chrome": 'http://www.baidu.com'
    }
    threads = []
    for browser,url in data.items():
        t = threading.Thread(target=baidu_search,args=(browser,url))
        threads.append(t)
    for thr in threads:
        thr.start()