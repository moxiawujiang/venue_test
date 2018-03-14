__author__ = 'wujiang'
#coding:utf-8
from venue_test.page.login_page import Login_Page

class Login_Page_Handle:
    def __init__(self,driver):
        self.lp=Login_Page(driver)
    #输入用户名
    def send_user_keys(self,username):
        self.lp.send_key(self.lp.get_user_element(),username)
    #输入密码
    def send_password(self,password):
        self.lp.send_key(self.lp.get_password_element(),password)
    #点击登录
    def login_botn_click(self):
        self.lp.click(self.lp.get_login_botn())

