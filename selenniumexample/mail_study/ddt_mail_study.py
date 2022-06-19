# !/usr/bin python3
# encoding: utf-8 -*-
# @file     :ddt_mail_study.py
# @author   : 声培 
# @Time     : 2022/6/20 0020 0:28
import smtplib      #调用SMTP发件服务
import unittest
from email.mime.text import MIMEText    #导入纯文本的邮件模板类
from email.mime.multipart import MIMEMultipart

import ddt

Data = ['2478703203@qq.com','2660676822@qq.com']

@ddt.ddt
class TestSendMail(unittest.TestCase):
    @ddt.data(*Data)
    def test_sendMail(self,mail):
        smtpserver = 'smtp.qq.com'      #QQ邮箱服务器
        sender = '761338269@qq.com'     #发送者邮箱
        psw = 'bznipopoeqngbchg'        #配置邮箱客户端生成的QQ邮箱授权码，乱写的，不可泄露，需要重新生成
        receiver = mail                 #接收者邮箱
        port = 465                      #QQ邮箱服务器默认端口号

        filepath = r'./1.jpeg'
        # with open as  代表打开文件后，用完默认调用close()
        with open(filepath, 'rb') as fp:
            mail_body = fp.read()

        msg = MIMEMultipart()
        msg["from"] = sender
        msg["to"] = receiver
        msg["suject"] = "带附件的邮件发送模板"
        body = MIMEText("美女跟你说晚安了", "html", "utf-8")
        msg.attach(body)
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment;filename="test_report.jpeg"'
        msg.attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp = smtplib.SMTP_SSL(smtpserver, port)  # 调用发送服务
            smtp.login(sender, psw)
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, port)
            smtp.login(sender, psw)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

if __name__ == '__main__':
    unittest.main()


