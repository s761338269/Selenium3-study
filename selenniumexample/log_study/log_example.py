# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :log_example.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 23:52

import logging

# logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# logger = logging.getLogger(__name__)
# logger.info("开始：输出Logging 日志")
# logger.debug("这是显示Debug级别的日志信息")
# logger.warning("这是显示Warning级别的日志信息")
# logger.info("结束：输出Logging日志")

#FATAL  致命错误
# INFO  处理请求或状态变化的日常事务
# DEBUG 调试过程中使用DEBUG等级，如算法中每个循环的中间状态
# CRITICAL  特别糟糕的事情，如内存耗尽，磁盘不足，一般少用
# ERROR     发生错误，如IO操作失败或链接失败
# WARNING      发生重要的事情，但不是错误，例如用户登录密码错误。

#定义文件
logFile = logging.FileHandler('logTest.txt','a',encoding='utf-8') #'a'表示对日志进行追加 ， encoding='utf-8'避免日志出现中文出错
# 设置日志格式
fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
logFile.setFormatter(fmt)
#定义日志级别
LoggerMany = logging.Logger('logTest',level=logging.DEBUG)  #设置日志级别
LoggerMany.addHandler(logFile)
#写入内容到logging日志
LoggerMany.critical('info')
# 输出日志信息
LoggerMany.info("开始：输出Logging 日志")
LoggerMany.debug("这是显示Debug级别的日志信息")
LoggerMany.warning("这是显示Warning级别的日志信息")
LoggerMany.info("结束：输出Logging日志")

