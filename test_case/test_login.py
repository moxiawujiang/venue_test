__author__ = '芜疆'
#coding=utf-8

import unittest
import time
import os
import sys
dir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir)
from selenium import webdriver
from public.base  import get_element,error_get_screen
from ddt import ddt,data,unpack
from  selenium.webdriver.common.action_chains import ActionChains

@ddt
class Login(unittest.TestCase):

    driver=webdriver.Firefox()
    @classmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()



    @error_get_screen(driver)
    def test_a_get_url(self):
        '''访问系统首页'''
        self.driver.get("")
        time.sleep(2)
        raise Exception("主动报错")


    @data(('4565uhggg','5466'),("test",'guhihi'),("",''),('admin',''))
    @unpack
    @error_get_screen(driver)
    def test_login_error(self,uname,pwrd):
        '''登陆失败场景'''
        username=get_element(self,"name","username")
        password=get_element(self,"name","password")
        username.clear()
        password.clear()
        username.send_keys(uname)
        password.send_keys(pwrd)
        login_botn=get_element(self,"id",'loginBtn')
        login_botn.click()
        time.sleep(2)
        self.assertEqual(self.driver.title,u'登录')
        error=get_element(self,"id",'error').text

        if error == u'用户名或密码错误'or u'请输入用户名' or u'请输入密码':
            pass
        else:
            raise Exception("登录失败提示不正确")


    @data(('test','test'),("admin","admin"))
    @unpack
    @error_get_screen(driver)
    def test_login_and_logout(self,uname,pwrd):
        username=get_element(self,"name","username")
        password=get_element(self,"name","password")
        username.clear()
        password.clear()
        username.send_keys(uname)
        password.send_keys(pwrd)

        login_botn=get_element(self,"id","loginBtn")
        login_botn.click()

        role_name=get_element(self,"classname","role-name")
        ActionChains(self.driver).move_to_element(role_name).perform()
        time.sleep(2)
        personal=get_element(self,"linktext",u"个人中心")
        personal.click()
        time.sleep(1)

        self.driver.switch_to.frame("mainFrame")
        real_name=get_element(self,"xpath",".//*[@id='personal_info_form']/div[3]/div[1]/div[2]")
        self.assertEqual(uname,real_name.text,u'登录用户信息错误')


        target = get_element(self,'xpath',".//*[@id='personal_info_form']/div[6]/button[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", target)#滑动至目标显示
        time.sleep(2)
        target.click()

        self.driver.switch_to.default_content()
        role_name1=get_element(self,"css",".role-name>a>span")
        ActionChains(self.driver).move_to_element(role_name1).perform()
        time.sleep(1)
        logout=get_element(self,"linktext","退出")
        logout.click()
        time.sleep(1)



if __name__ == '__main__':
    unittest.main()
