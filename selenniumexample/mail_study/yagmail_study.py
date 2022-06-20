# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :yagmail_study.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 1:45

import smtplib,yagmail
#调用SMTP发件服务
from email.mime.text import MIMEText    #导入纯文本的邮件模板类
from email.mime.multipart import MIMEMultipart


yagindex = yagmail.SMTP(user="76******69@qq.com",password='bz******bchg',host='smtp.qq.com')
Yag_contents = ['这是一个yagmail发送邮件正文的实例']
yagindex.send(['24******03@qq.com','761*****9@qq.com'],'Yagmail主题实例',Yag_contents)

# 发送带附件的邮件
yagindex = yagmail.SMTP(user="761338269@qq.com",password='bznipopoeqngbchg',host='smtp.qq.com')
Yag_contents = ['这是一个yagmail发送邮件正文的实例']
yagindex.send(['24******203@qq.com','76******69@qq.com'],'Yagmail主题实例',Yag_contents,[r"E:\pythonProject\selennium3_study\selenniumexample\mail_study\1.jpeg"])