from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.chrome()
    #driver = webdriver.Chrome('C:/Users/varsh/Desktop/TheFirstOne/chromedriver_win32/chromedriver.exe')
    return driver

