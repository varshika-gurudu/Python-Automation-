from selenium import webdriver
from selenium.webdriver.common.by import By

#creating page object for login page

class LoginPageFirst:
    text_box_username_id = 'Email'
    text_box_password_id = 'Password'
    login_button_xpath = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    link_logout_link_text = 'Logout'

    def __init__(self,driver):
        self.driver = driver

        #clear the username text box before sending the keys

    def setUsername(self, username):
        self.driver.find_element_by_id(self.text_box_username_id).clear()
        self.driver.find_element_by_id(self.text_box_username_id).send_keys(username)

        #clear the password text box before sending password

    def setPassword(self, password):
        self.driver.find_element_by_id(self.text_box_password_id).clear()
        self.driver.find_element_by_id(self.text_box_password_id).send_keys(password)

        #clicking login button

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

        #logout

    def clickLogout(self, link_logout_link_text=None):
        self.driver.find_element_by_link_text(link_logout_link_text).click()

