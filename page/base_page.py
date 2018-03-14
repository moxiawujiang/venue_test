__author__ = 'wujiang'
#coding:utf-8
from venue_test.public.driver_base import Driver_Base

class Base_Page:
    def __init__(self,driver):
        self.driver=Driver_Base(driver)

    #封装定位
    def get_element(self,by,local):
        return  self.driver.find_element(by,local)

    #封装点击
    def click(self,element):
        if element!=None:
            element.click()
        else:
            raise Exception(u'元素没有定位到，点击失败')

    #封装输入
    def send_key(self,element,value):
        return element.send_keys(value)

    #封装显示
