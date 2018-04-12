__author__ = 'wujiang'
#coding:utf-8
from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
import time
import re

def test_search():
    driver=webdriver.Firefox()
    driver.get("http://www.baidu.com/")
    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element_value((By.XPATH,"html']"),u'百度一下'))

    time.sleep(3)
    driver.quit()

    #输入一个文件和一个字符串，打印出字符串在文件中出现的次数
def test001(filename=None,str=None):
    fp=open('./geckodriver.log')
    filetext=fp.read()
    print(filetext.count("version"))
    # list=re.findall(str,filetext)
    # print(len(list))

    #找出一个字符串在另一个字符串中出现的次数,以及第一次出现的位置
def test002():
    s1="nihhihanotiananmen"
    s2="an"
    print(s1.count(s2))
    print(s1.find(s2))
    print(s1[3:10])







if __name__ == '__main__':
    test001()