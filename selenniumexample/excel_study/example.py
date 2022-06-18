# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :example.py
# @author   : 声培 
# @Time     : 2022/6/19 0019 0:46
import xlrd
def readUsername(row):
    '''读取用户名'''
    book = xlrd.open_workbook('data.xls','r')
    table = book.sheet_by_index(0)  #获取第一个sheet表
    # 获取设定的你选定一列的数据
    print(table.row_values(row)[1])
    return table.row_values(row)[1]
if __name__ == '__main__':
    readUsername(1)