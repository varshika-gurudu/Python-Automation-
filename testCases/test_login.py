from selenium import webdriver
from pageObjects.LoginPage import LoginPageFirst
import pytest
from utilities.readUtilities import ReadConfig
from utilities.customLogger import LogGen

#test cases

class Test_001_Login:

    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    #checking if the base URL working

    #@pytest.mark.regression
    def test_HomeTitlePage(self,setup):

        self.logger.info('*********test_HomeTitlePage***********')
        self.logger.info('******started verifying login page title********')
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == 'Your store. Login':
            self.logger.info('*********Home page title is passed***********')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot('.\\Screenshots\\'+ 'test_HomeTitlePage.png')
            self.logger.info('*********Home page title is Failed***********')
            self.driver.close()
            assert False

    #checking if the login by entering valid username and password

    def test_login_page(self,setup):
        #self.driver = webdriver.Chrome('C:/Users/varsh/Desktop/chromedriver_win32/chromedriver.exe')
        self.logger.info('*********verifying login test***********')
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPageFirst(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            self.logger.info('*********login is passed***********')
            assert True
        else:
            self.logger.info('*********Home page title is Failed***********')
            assert False
        self.driver.close()












