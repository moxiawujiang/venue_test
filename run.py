__author__ = '芜疆'
#coding=utf-8
from selenium import  webdriver
import unittest
import time
import HTMLTestRunner
import test_case
import os
import sys
os.chdir(sys.path[0])
from os import path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_my_suit():
    my_suit=unittest.TestSuite()
    testdir="test_case"
    discover=unittest.defaultTestLoader.discover(testdir,pattern="test*.py",top_level_dir=None)
    for test_suit in discover:
        for test_case in  test_suit:
            my_suit.addTest(test_case)
    return my_suit

def send_report(file_dir):

    report_dir=path.dirname(__file__)+"\\"+file_dir
    #获取目录下的所有文件
    lists=os.listdir(report_dir)
    lists.sort(key=lambda fn:os.path.getmtime(report_dir+"\\"+fn))

    # 将文件目录与文件名进行拼接，从而打印出目录下最新文件的绝对路径
    new_report=os.path.join(report_dir,lists[-1])

    mail_from="13709048313@163.com"
    mail_to=["www.6058332571@qq.com","273439708@qq.com"]


    msg=MIMEMultipart()
    #构造正文
    f=open(new_report,'rb')
    mail_body=f.read()
    f.close()
    text=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(text)

    #构造附件
    att=MIMEText(mail_body,"base64",'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att)


    msg["Subject"]=u"体育场馆自动化测试报告"
    msg["From"]=mail_from
    msg["To"]=",".join(mail_to) #接收者多个账号使用,链接，传入类型是str

    smtp=smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("13709048313@163.com","605332571qwe")
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    currenttime=time.strftime("%y-%m-%d %H-%M-%S")
    filedir="test_report\\"
    reportdir=filedir+currenttime+".html"
    fp=open(reportdir,"w",encoding="utf-8")
    runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,title=u"场馆测试报告",description=u"用例执行情况")
    my_suit=create_my_suit()
    runner.run(my_suit)
    fp.close()
    time.sleep(3)
    #send_report(filedir)







