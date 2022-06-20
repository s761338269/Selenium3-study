# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :main.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 18:22
import HTMLTestRunner
import os
import time
import unittest

# file = open(os.path.join(os.path.dirname(__file__),'reports',time.strftime("%Y_%m_%d_%H_%M_%S")+ 'report.html'),'wb')
# # 生成的报告描述
# run = HTMLTestRunner.HTMLTestRunner(stream=file, title="测试报告",description="执行结果")
# #用例目录
# dis = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),'TestCases'),pattern='test_*.py')
# run.run(dis)

def getAllCases():
    """获取testcase下的所有测试模块"""
    dis = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),'TestCases'),pattern='test_*.py')
    return dis
def RunMain():
    """生成测试报告，写入指定Report是目录"""

    file = open(os.path.join(os.path.dirname(__file__),'reports',time.strftime("%Y_%m_%d_%H_%M_%S")+ 'report.html'),'wb')
    # 生成的报告描述
    run = HTMLTestRunner.HTMLTestRunner(stream=file, title="测试报告",description="执行结果").run(getAllCases())

if __name__ == '__main__':
    RunMain()
