# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :mail_study.py
# @author   : 声培 
# @Time     : 2022/6/19 0019 15:47
import smtplib      #调用SMTP发件服务
from email.mime.text import MIMEText    #导入纯文本的邮件模板类


smtpserver = 'smtp.qq.com'      #QQ邮箱服务器
sender = '76169@qq.com'     #发送者邮箱
psw = 'omkcgazbai'        #配置邮箱客户端生成的QQ邮箱授权码，乱写的，不可泄露，需要重新生成
receiver = '24783@qq.com'  #接收者邮箱
port = 465                      #QQ邮箱服务器默认端口号

body = '这是一封测试邮件'
msg =MIMEText(body,'html','utf-8')  #邮件正文内容
msg['from'] = '7669@qq.com'    #发送者账号
msg['to'] = '247873@qq.com'     #接收者账号
msg['subject'] = "这个是纯文本发送的邮件示例"    #邮件标题

smtp = smtplib.SMTP_SSL(smtpserver,port)    #调用发送服务
smtp.login(sender,psw)                      #通过发送者账号和授权码登录邮箱
smtp.sendmail(sender,receiver,msg.as_string())  #发送件，信息以字符串方式保存
smtp.quit()         #关闭邮件服务

