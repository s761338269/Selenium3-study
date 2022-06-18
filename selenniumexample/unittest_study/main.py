# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :main.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 11:39
import time
import unittest,os
import HTMLTestRunner

# # 方法一：自己根据绝对路径找存放地址
# report_path = 'E:\\pythonProject\\selennium3_study\\selenniumexample\\unittest_study\\Reports\\'
# test_path = r'E:\\pythonProject\\selennium3_study\\selenniumexample\\unittest_study\\TestCase'
# 第一步，报告的存放地址
file = open(os.path.join(os.path.dirname(__file__),'reports',time.strftime("%Y_%m_%d_%H_%M_%S")+ 'report.html'),'wb')
# 生成的报告描述
run = HTMLTestRunner.HTMLTestRunner(stream=file, title="测试报告",description="执行结果")
#用例目录
dis = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),'TestCase'),pattern='test_*.py')
run.run(dis)