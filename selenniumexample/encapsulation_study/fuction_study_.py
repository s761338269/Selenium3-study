# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :fuction_study_.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 13:33

#按照方法对代码进行封装
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# expected_conditions函数，一单出现这个元素就执行
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def Element_Locatior(*new_loctor):
    """重写find_elemnet定位方法"""
    return driver.find_element(*new_loctor)

def input_username(username,*userLoctor):
    """输入用户名"""
    return Element_Locatior(*userLoctor).send_keys(username)

def input_password(password,*pwdLoctor):
    """输入密码"""
    return Element_Locatior(*pwdLoctor).send_keys(password)

def click_btn(*btnLoctor):
    """点击登录按钮"""
    return Element_Locatior(*btnLoctor).click()

def assert_Login_text(*assertText):
    """获取登录成功后的验证信息"""
    return Element_Locatior(*assertText).text

if __name__ == '__main__':

    user_loc = (By.ID,'phone')
    pwd_loc = (By.ID,'pwd')
    btn_loc = (By.ID,'loginBtn')
    suceeLogin_loc = (By.CSS_SELECTOR,'#siteName')
    suceeLogin_loc1 = (By.CSS_SELECTOR,'#err-txt')


    driver = webdriver.Firefox()
    driver.get('https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https%3A%2F%2Fi.chaoxing.com')
    driver.maximize_window()
    sleep(3)
    driver.refresh()
    input_username('17306687410',*user_loc)
    input_username('a767826912', *pwd_loc)
    click_btn(*btn_loc)
    try:
        element = WebDriverWait(driver, 3, 0.5).until(expected_conditions.presence_of_element_located(suceeLogin_loc))
        if element.text =='广州航海学院':
            print('测试通过')
        else:
            print('测试失败')
    except Exception as message:
        element = WebDriverWait(driver, 3, 0.5).until(expected_conditions.presence_of_element_located(suceeLogin_loc1))
        if element.text =='手机号或密码错误':
            print(message)
            print(element.text)
        else:
            print('测试失败')

    driver.quit()




