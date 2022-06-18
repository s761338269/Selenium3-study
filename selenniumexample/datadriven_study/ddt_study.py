# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :ddt_study.py
# @author   : 声培 
# @Time     : 2022/6/18 0018 17:18

import ddt
import unittest

# Data =[
#         {'name':'Keep learing'},
#         {'age':18},
#         {'address':'广州'}
#        ]
#需要再测试类使用@ddt.ddt装饰器，在测试用例上使用@ddt.data装饰器
# @ddt.data()装饰器，参数可以是单个值，列表，元组或字典
#对于列表和元组，需要用到@ddt.unpack装饰器吧元组和列表解析成多个参数

# # 参数为单个值
# @ddt.ddt
# class TestMoules(unittest.TestCase):
#     def setUp(self) -> None:
#         print('测试开始')
#
#     def tearDown(self) -> None:
#         print('测试结束')
#     #使用@ddt.data(Data),将Data数据组传给测试用例
#     @ddt.data(*Data)
#     def test_DataDriver(self,Data):
#         print('DDT数据驱动实战演示，分别执行每组数据：',Data)

Data  = [
    ['admin','123456','账号或密码错误'],
    ['xiaochen','123456','登录成功'],
    ['admin','','登录失败'],
    ['','123456','登录失败']
]


# 使用@ddt.data(Data),将Data数据组传给测试用例
@ddt.ddt
class TestMoules(unittest.TestCase):
    def setUp(self) -> None:
        print('测试开始')

    def tearDown(self) -> None:
        print('测试结束')

    @ddt.data(*Data)
    @ddt.unpack
    def test_DataDriver(self,user,password,text):
        print('DDT数据驱动实战演示，账号：',user)
        print('DDT数据驱动实战演示，密码：', password)
        print('DDT数据驱动实战演示，登录状态：', text)

if __name__ == '__main__':
    unittest.main()
