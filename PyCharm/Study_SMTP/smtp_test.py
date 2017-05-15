# !/usr/bin/python
# coding:utf-8

import smtplib

from email.mime.text import MIMEText
from email.header import Header

sender = 'test@test.com'
receives = ['test2@test.com']

message = MIMEText('Pthon 邮件发送测试','plain','utf-8')
message['From'] = Header('Test','utf-8')
message['To'] = Header('测试','utf-8')

subject = 'Python SMTP 邮件测试'
message['Subkect'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receives,message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "邮件无法发送"