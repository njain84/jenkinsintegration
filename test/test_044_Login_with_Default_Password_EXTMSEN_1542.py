from selenium import webdriver
from configparser import ConfigParser
from Login_config.LoginHandleradminportal import Loginmsadmin
import pytest

class default_password():

    def test_login_with_default_password(self):
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        myloginadmin = Loginmsadmin('admin', 'Harman12#$', parser.get('bug_tracker', 'url'), driver)
        myloginadmin.doLoginadmin()
        driver.implicitly_wait(10)
        # it will get te test as Confirmation fom the Confirmation page
        Actual_text = driver.find_element_by_id('dialogModalLabel').text
        print(Actual_text)
        Expected_text = 'Confirmation'
        assert Actual_text == Expected_text, 'EXTMSEN-1652-Assert error:Confirmation page is not available'


