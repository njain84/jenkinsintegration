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

class Add_admin_user(unittest.TestCase):

    def test_add_admin_user(self):
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)

        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)

        deleteuserandcreateauditor = adminportal_user_tab(self.driver)
        deleteuserandcreateauditor.delete_user()
        time.sleep(2)
        deleteuserandcreateauditor.add_admin_user()
        time.sleep(5)

#--------------------------------------------
        # It will count the total row an column
        #trows = len(self.driver.find_elements_by_xpath("//table/tbody/tr"))
        #print("the number of records are:", trows)
        #Tcolumn = len(self.driver.find_elements_by_xpath("//*[@id='mainForm:userPanel_body']/div[3]/table/thead/tr/th"))
        #print("the number of records are:", Tcolumn)
        #n = 0
        #b="//*[@id='user-table-row-n']/td[2]"
        #while n<=trows:
            #b = '''"//*[@id='user-table-row-'''+str(n)+'''']/td[2]"'''
            #print(b)

            #Username= self.driver.find_element_by_xpath b.text

            #Username1 = self.driver.find_element_by_xpath("//*[@id='user-table-row-0']/td[2]")

            #print(Username)
            #n = n + 1#
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
        # confirm password

        self.driver.find_element_by_id('modalForm:PWD-oldPwd').send_keys('123')
        self.driver.find_element_by_id('modalForm:PWD-newPwd').send_keys('123')
        self.driver.find_element_by_id('modalForm:PWD-confirmPwd').send_keys('123')
        time.sleep(3)
        self.driver.find_element_by_id('setPwd-blt').click()

        self.driver.find_element_by_id('a_1000').is_displayed()

        time.sleep(4)
        # login user portal
        self.driver.get(parser.get('bug_tracker', 'urluserportal'))
        self.driver.find_element_by_id('login_user').send_keys('scriptadmin', Keys.TAB)
        print("Hi")

        self.driver.find_elements_by_class_name('form-control')[1].send_keys('123')

        self.driver.find_elements_by_class_name('btn')[0].click()

        time.sleep(5)
        result = self.driver.find_elements_by_class_name('btn')[0].text
        print(result)
        actual_result = 'Start Recording'
        assert actual_result == result, 'Fail'
        self.driver.quit()







