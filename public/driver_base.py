__author__ = 'wujiang'
#coding:utf-8
from  selenium  import  webdriver


class Select_Driver:
    def __init__(self,driver):
        self.driver=driver
    def select_driver(self):
        if self.driver=="firefox" or"FireFox":
            return webdriver.Firefox()
        elif self.driver=="Chrome" or "chrome":
            return webdriver.Chrome()

class Driver_Base:
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,by,local):
         try:
            if by=='id':
                return self.driver.find_element_by_id(local)
            elif by=='name':
                return self.driver.find_element_by_name(local)
            elif by=="classname":
                return self.driver.find_element_by_class_name(local)
            elif by=="xpath":
                return self.driver.find_element_by_xpath(local)
            elif by=="css":
                return self.driver.find_element_by_css_selector(local)
            elif by=="linkname":
                return self.driver.find_element_by_link_name(local)
            elif by=="linktext":
                return self.driver.find_element_by_link_text(local)
            else:
                raise Exception("没有这种定位方式")
         except Exception as e:
             raise e


