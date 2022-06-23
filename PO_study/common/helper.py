# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :helper.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 20:12
import logging
import os.path
# cmd 运行pytest找不到路径时可以用
import sys
sys.path.append(os.getcwd())
import xlrd


class Helper:
    def readExcels(self,rowx):
        """

        :param rowx:是行数
        :return: 返回的一共有多少行
        """
        # unittest执行就用这个r'..\data\data.xls'
        # pytest执行用'.\data\data.xls'
        book = xlrd.open_workbook(r'..\data\data.xls','r')
        table = book.sheet_by_index(0)
        return table.row_values(rowx)

    def readusername(self,rowx):
        """

        :param rowx: 代表返回的是第几行
        :return:    返回第rowx行的用户名
        """
        return str(self.readExcels(rowx)[0])


    def readuserpsd(self,rowx):
        """

        :param rowx: 代表返回的是第几行
        :return:    返回第rowx行的密码
        """
        return str(self.readExcels(rowx)[1])

    def exceptText(self,rowx):
        """

        :param rowx: 代表返回的是第几行
        :return:    返回第rowx行的预期结果
        """
        return str(self.readExcels(rowx)[2])

    def dirname(self,filename,filepath='data'):
        """
        生成测试报告时，需要用例路径或者生成路径可能会用到
        :param filename: 文件名
        :param filepath: 文件路径
        :return:
        """
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)

    def log(self,log_content):
        """定义日志级别"""
        logFile = logging.FileHandler('log.txt', 'a', encoding='utf-8')
        # 设置日志格式
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        logFile.setFormatter(fmt)
        # 定义日志
        logger1 = logging.Logger('logTest', level=logging.DEBUG)
        logger1.addHandler(logFile)
        logger1.info(log_content)
        logFile.close()