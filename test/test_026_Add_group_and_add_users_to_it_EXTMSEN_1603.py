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

class Create_group(unittest.TestCase):

    def test_create_group(self):
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        pyautogui.FAILSAFE = False
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')

        start= adminportal_user_tab(self.driver)
        start.delete_multiple_user_and_group()
        time.sleep(2)
        start.add_multiple_users()
        time.sleep(2)
        result=start.Group()
        print(result)
        actual_result = '2'
        assert actual_result == result, 'EXTMSEN_1603 is failed'
        time.sleep(5)
        self.driver.close()




