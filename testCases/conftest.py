from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    #driver = webdriver.chrome()
    if browser == 'chrome':
        driver = webdriver.Chrome('C:/Users/varsh/Desktop/TheFirstOne/chromedriver_win32/chromedriver.exe')
        print('Launching chrome browser')
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='C:/Users/varsh/Desktop/geckodriver-v0.29.1-win64/geckodriver.exe')
        print("Launching firefox browser.........")
        return driver



def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Varshika'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

