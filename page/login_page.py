__author__ = 'wujiang'
#coding:utf-8
from venue_test.page.base_page import Base_Page


class Login_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)

    #获取用户名框
    def get_user_element(self):
        return Base_Page.get_element(self,"name","username")

    #获取密码框
    def get_password_element(self):
        return  Base_Page.get_element(self,"name","password")
    #获取登录按钮
    def get_login_botn(self):
        return Base_Page.get_element(self,"id","loginBtn")






