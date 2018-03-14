__author__ = '芜疆'
#encoding=utf-8
import time
import os
from  selenium import webdriver
#封装定位方法
def get_element(self,by,local):
    driver=self.driver
    try:
        if by=='id':
            return driver.find_element_by_id(local)
        elif by=='name':
            return driver.find_element_by_name(local)
        elif by=="classname":
            return  driver.find_element_by_class_name(local)
        elif by=="xpath":
            return driver.find_element_by_xpath(local)
        elif by=="css":
            return driver.find_element_by_css_selector(local)
        elif by=="linkname":
            return driver.find_element_by_link_name(local)
        elif by=="linktext":
            return driver.find_element_by_link_text(local)
        else:
            raise Exception("没有这种定位方式")
    except Exception as e:
            raise e

#封装截图并储存
def get_screen_and_print_pic_path(self):
    driver=self.driver
    current_time=time.strftime("%y-%m-%d %H-%M-%S")
    pic_path=get_path(2)+"\\test_report\\image\\"+current_time+".png"
    driver.save_screenshot(pic_path)
    print('picture:'+pic_path+":end")



#封装获取需要的目录
def get_path(n):
    dir=__file__
    for i in range(n):
        dir=os.path.dirname(dir)
    return dir

#失败截屏装饰器
class error_get_screen(object):

    def __init__(self,driver):
        self.driver=driver

    def __call__(self, func):
        def f2(*args,**kwargs):
            try:
                func(*args,**kwargs)
            except:
                get_screen_and_print_pic_path(self)
                raise
        return f2



#封装随机选择下拉框操作
def select_box(driver,xpath):
    s=driver.find_elements_by_xpath(xpath)
