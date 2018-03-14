__author__ = 'wujiang'
#coding:utf-8
from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
import time

def test_search():
    driver=webdriver.Firefox()
    driver.get("http://www.baidu.com/")
    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element_value((By.XPATH,"html']"),u'百度一下'))

    time.sleep(3)
    driver.quit()







if __name__ == '__main__':
    test_search()