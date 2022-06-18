# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :ddt_study3.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 21:02
from time import sleep

from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By

dr = webdriver.Firefox()
dr.get('https://mail.sohu.com/fe/#/login')
sleep(2)
dr.find_element(By.CSS_SELECTOR,".addFocus.ipt-account.ng-pristine.ng-valid").send_keys('123456')
