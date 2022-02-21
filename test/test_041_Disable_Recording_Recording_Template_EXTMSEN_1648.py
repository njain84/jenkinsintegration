import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
import unittest
import openpyxl
from configparser import ConfigParser
from .POM.EPlogin_callhangup import Ephangup
from .POM.POM_admin_template import admin_Template
from .POM.POM_admin_call_dial_in_out import admin_call


class Disable_Recording(unittest.TestCase):

    def test_Disable_Recording(self):
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        try:
            template = admin_Template(driver)
            template.navigate_to_template()
            time.sleep(2)
            template.add_new_template()
            time.sleep(2)
            template.create_vrr()
            call = admin_call(driver)
            call_final = call.admin_dialouttorecord_choose_VRR()
            print(call_final[0])
            print(call_final[1])
            assert call_final[0] < call_final[1], "EXTMSEN-1648-Assert error:File is created however it should not be created"
        finally:

            try:
                driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
                template = admin_Template(driver)
                template.navigate_to_template()
                template.delete_template()
                template.delete_vrr()
                parser = ConfigParser()
                configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
                parser.read(configFilePath)
                time.sleep(2)
                call_hangup = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
                call_hangup.doepcallhangup()
            except WebDriverException as e:
                print('error',e)

    if __name__ == '__main__':
        unittest.main()
