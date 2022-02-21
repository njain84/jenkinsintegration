import time
import logging
from selenium import webdriver
import pyautogui
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys

from Login_config.LoginHandleradminportal import Loginmsadmin
from configparser import ConfigParser
import unittest
import openpyxl
import allure
import pytest
from configparser import ConfigParser
from Login_config.LoginHandler import Loginms
from datetime import datetime
from datetime import datetime as dt
from selenium.webdriver.support.ui import Select
from .POM.POM_admin_user_tab import adminportal_user_tab

class Add_user(unittest.TestCase):

    def test_add_user(self):
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)

        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        deleteuserandcreateauditor = adminportal_user_tab(self.driver)
        deleteuserandcreateauditor.delete_user()
        time.sleep(2)
        deleteuserandcreateauditor.add_user()

# --------------------------------------------
# login the admin portal
        self.driver.get(parser.get('bug_tracker', 'url'))
        time.sleep(5)
        self.driver.find_element_by_id('loginForm:userName').send_keys('scriptadmin')
        print("Hi")
        time.sleep(2)
        self.driver.find_element_by_id('loginForm:password').send_keys('123')
        time.sleep(3)
        self.driver.find_element_by_id('loginBtton').click()
        time.sleep(3)
        login_text = self.driver.find_element_by_id('infoDetail').text
        print(login_text)
        actual_login_text = 'You are not an authorized user.'
        assert actual_login_text == login_text,'User can login admin portal,EXTMSEN_1602'
#-----------------------------------------------------------
 # login user portal
        self.driver.get(parser.get('bug_tracker', 'urluserportal'))
        self.driver.find_element_by_id('login_user').send_keys('scriptadmin',Keys.TAB)
        print("Hi")

        self.driver.find_elements_by_class_name('form-control')[1].send_keys('123')

        self.driver.find_elements_by_class_name('btn')[0].click()
        time.sleep(5)
        self.driver.find_element_by_id('oldPwd').send_keys('123',Keys.TAB,'123',Keys.TAB,'123',Keys.TAB,Keys.TAB,Keys.ENTER)
        time.sleep(2)
        result=self.driver.find_elements_by_class_name('btn')[0].text
        print(result)
        actual_result = 'Start Recording'
        assert actual_result == result,'Fail'
        self.driver.quit()










