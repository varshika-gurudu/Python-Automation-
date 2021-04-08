from selenium import webdriver
from pageObjects.LoginPage import LoginPageFirst
import pytest

#test cases

class Test_001_Login:

    base_url = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
    username = 'admin@yourstore.com'
    password = 'admin'

    #checking if the base URL working

    def test_HomeTitlePage(self,setup):
        #self.driver = webdriver.Chrome('C:/Users/varsh/Desktop/chromedriver_win32/chromedriver.exe')
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == 'Your store. ogin':
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+ 'test_HomeTitlePage.png')
            self.driver.close()
            assert False

    #checking if the login by entering valid username and password

    def test_login_page(self,setup):
        #self.driver = webdriver.Chrome('C:/Users/varsh/Desktop/chromedriver_win32/chromedriver.exe')
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPageFirst(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
        else:
            assert False
        self.driver.close()












