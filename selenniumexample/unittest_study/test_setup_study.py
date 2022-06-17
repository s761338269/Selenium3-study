# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :test_setup_study.py
# @author   : 声培 
# @Time     : 2022/6/17 0017 22:49
import unittest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    # 前置操作
    @classmethod
    def setUpClass(cls) -> None:
        cls.dr = webdriver.Firefox()
        url = 'https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com'
        cls.dr.get(url)
        sleep(2)

    # def setUp(self) -> None:
    #     self.dr = webdriver.Firefox()
    #     url = 'https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com'
    #     self.dr.get(url)
    #     sleep(2)

    # 用例一：成功登录学习通
    def test_1(self):
        # self.dr.find_element(By.ID,'phone').send_keys('123456789')
        # sleep(2)
        # self.dr.find_element(By.ID,'pwd').send_keys('123456')
        # sleep(0.5)
        # self.dr.find_element(By.ID,'loginBtn').click()
        # self.assertEqual(self.dr.title,'个人空间','页面跳转失败')
        print(1)
    # 用例一：账号密码错误
    def test_2(self):
        # self.dr.find_element(By.ID,'phone').send_keys('1234567891')
        # sleep(2)
        # self.dr.find_element(By.ID,'pwd').send_keys('000000000')
        # sleep(0.5)
        # self.dr.find_element(By.ID,'loginBtn').click()
        # self.assertEqual(self.dr.title,'用户登录','登录界面出现异常')
        print(2)

    # 用例3：输出3
    def test_3(self):
        print(3)


    # # 后置操作
    # def tearDown(self) -> None:
    #     self.dr.quit()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.dr.quit()

class Test_2(unittest.TestCase):
    # 前置操作
    # def setUp(self) -> None:
    #     self.dr = webdriver.Firefox()
    #     url = 'https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com'
    #     self.dr.get(url)
    #     sleep(2)

    # 用例一：成功登录学习通
    def test_4(self):
        # self.dr.find_element(By.ID,'phone').send_keys('123456789')
        # sleep(2)
        # self.dr.find_element(By.ID,'pwd').send_keys('123456')
        # sleep(0.5)
        # self.dr.find_element(By.ID,'loginBtn').click()
        # self.assertEqual(self.dr.title,'个人空间','页面跳转失败')
        print(4)
    # 用例一：账号密码错误
    def test_5(self):
        # self.dr.find_element(By.ID,'phone').send_keys('1234567891')
        # sleep(2)
        # self.dr.find_element(By.ID,'pwd').send_keys('000000000')
        # sleep(0.5)
        # self.dr.find_element(By.ID,'loginBtn').click()
        # self.assertEqual(self.dr.title,'用户登录','登录界面出现异常')
        print(5)

    # 用例3：输出3
    def test_6(self):
        print(6)


    # # 后置操作
    # def tearDown(self) -> None:
    #     self.dr.quit()

if __name__ == '__main__':
    # 执行全部用例
    # unittest.main()

    # 执行一个类里的特定方法
    # 创建套件
    suit = unittest.TestSuite()
    # 添加用例
    suit.addTest(Test('test_3'))
    # 执行用例
    run = unittest.TextTestRunner()
    run.run(suit)

    # 执行某个类
    # 创建套件
    suit = unittest.TestSuite()
    # 创建load对象加载类
    load = unittest.TestLoader
    # 添加指定类
    suit.addTest(load.loadTestsFromTestCase(Test_2))
    # 执行类的用例
    run = unittest.TextTestRunner()
    run.run(suit)

