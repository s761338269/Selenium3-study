# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :main.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 18:22
import HTMLTestRunner
import os
import smtplib
import time
import unittest

# file = open(os.path.join(os.path.dirname(__file__),'reports',time.strftime("%Y_%m_%d_%H_%M_%S")+ 'report.html'),'wb')
# # 生成的报告描述
# run = HTMLTestRunner.HTMLTestRunner(stream=file, title="测试报告",description="执行结果")
# #用例目录
# dis = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),'TestCases'),pattern='test_*.py')
# run.run(dis)
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(file_new):
    # 基本信息
    smtpserver = 'smtp.qq.com'  # QQ邮箱服务器
    sender = '761338269@qq.com'  # 发送者邮箱
    psw = 'mk********bdai'  # 配置邮箱客户端生成的QQ邮箱授权码，乱写的，不可泄露，需要重新生成
    receiver = '2478703203@qq.com'  # 接收者邮箱
    port = 465  # QQ邮箱服务器默认端口号

    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    #定义邮件主题
    msg = MIMEMultipart()
    msg["from"] = sender
    msg["to"] = receiver
    msg["suject"] = Header("Page Object 自动化测试报告",'utf-8')
    #如果不加msg["from"]、msg["to"]会报错，因为发件人和收件人的参数没有定义
    body = MIMEText(mail_body,'html','utf-8')
    msg.attach(body)
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="test_report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp = smtplib.SMTP_SSL(smtpserver, port)  # 调用发送服务
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(msg["from"], psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("邮件发送成功")

#查看最新测试报告
def new_file(test_dir):
    result_dir = test_dir
    lists = os.listdir(result_dir)  #列出测试报告目录下的所有文件
    lists.sort()
    file = [x for x in lists if x.endswith('.html')]
    file_path = os.path.join(result_dir,file[-1])
    return file_path

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(base_dir,'testCases')
    test_report = os.path.join(base_dir,'reports')
    testlist = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    filename = test_report + '\\' + now +'report.html'
    fp = open(filename,'wb')
    # 生成的报告描述
    run = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Python+Selenium的自动化测试报告",description="系统环境win11，浏览器：火狐浏览器 用例执行情况")
    run.run(testlist)
    fp.close()
    new_report = new_file(test_report)
    send_mail(new_report)

