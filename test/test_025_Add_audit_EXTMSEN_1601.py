import time
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
import unittest
from configparser import ConfigParser
import openpyxl
from selenium.common.exceptions import TimeoutException, WebDriverException
import re
from selenium.webdriver.common.keys import Keys
from .POM.POM_admin_user_tab import adminportal_user_tab


class add_auditor_EXTMSEN_1601(unittest.TestCase):

    

    def test_check_audit_user(self):
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')

        mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)

        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)

        deleteuserandcreateauditor = adminportal_user_tab(self.driver)
        deleteuserandcreateauditor.delete_user()
        time.sleep(2)
        deleteuserandcreateauditor.Add_Auditor()

        time.sleep(1)

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
        # Confirm Password
        self.driver.find_element_by_id('modalForm:PWD-oldPwd').send_keys('123')
        self.driver.find_element_by_id('modalForm:PWD-newPwd').send_keys('123')
        self.driver.find_element_by_id('modalForm:PWD-confirmPwd').send_keys('123')
        time.sleep(3)
        self.driver.find_element_by_id('setPwd-blt').click()
        time.sleep(2)
        adminlogin = self.driver.find_element_by_id('a_1005').is_displayed()
        print('login',adminlogin)

        # -----------------------------------------------------------
        # login user portal
        self.driver.get(parser.get('bug_tracker', 'urluserportal'))
        self.driver.find_element_by_id('login_user').send_keys('scriptadmin', Keys.TAB)
        print("Hi")

        self.driver.find_elements_by_class_name('form-control')[1].send_keys('123')

        self.driver.find_elements_by_class_name('btn')[0].click()
        time.sleep(3)

        # Verifying not authorization
        login_text = self.driver.find_elements_by_class_name('form-group')[5].text
        print('permission',login_text)
        actual_login_text = 'Not enough permission.'
        assert actual_login_text == login_text, 'Auditor can login user portal,EXTMSEN_1601'
        time.sleep(4)
        self.driver.quit()
