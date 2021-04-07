from selenium import webdriver
from pageObjects.LoginPage import LoginPageFirst
import pytest

#test cases

class Test_001_Login:

    base_url = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    username = 'admin@yourstore.com'
    password = 'admin'

    #checking if the base URL working

    def test_HomeTitlePage(self):
        self.driver = webdriver.Chrome('C:/Users/varsh/Desktop/chromedriver_win32/chromedriver.exe')
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == 'Your store. Login':
            assert True
        else:
            assert False

    #checking if the login by entering valid username and password

    def test_login_page(self):
        self.driver = webdriver.Chrome('C:/Users/varsh/Desktop/chromedriver_win32/chromedriver.exe')
        self.driver.get(self.base_url)
        self.lp = LoginPageFirst(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()












