# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :getImage.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 21:14
import os.path
import time


def SaveImage(driver,errorImage):
    """用例失败截图功能"""
    Rawpath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Image')
    NewPicture = Rawpath + '\\' + time.strftime('%Y_%m_%d_%H_%M_%S') + '_' + errorImage
    driver.get_screenshot_as_file(NewPicture)
