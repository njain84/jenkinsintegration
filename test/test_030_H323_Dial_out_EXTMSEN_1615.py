import unittest
import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
from .POM.POM_Registration import admin_Registration
from .POM.POM_admin_call_dial_in_out import admin_call

class admin_H323_dial_out_withoutdma(unittest.TestCase):

    def test_H323_dial_out_withoutdma(self):
        
        print("Hello....")
        # configur = ConfigParser()
        parser = ConfigParser()
        parser.read('config.ini')
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        time.sleep(2)
        registration = admin_Registration(driver)
        registration_status = registration.test_H323_unregister()
        print('Protocol is', registration_status)
        time.sleep(2)
        dialout_H323 = admin_call(driver)
        funtion_values = dialout_H323.admin_dialouttorecord_H323()
        print('values are:', funtion_values)
        driver.close()
        assert funtion_values[0] >= funtion_values[1], "EXTMSEN-1615-Assert error: Test case is failed because file is not created!"
        assert funtion_values[2] == "H323", "EXTMSEN-1615-Assert error: Test case is failed because protocol is not H323!"
        assert registration_status != 'Online', "EXTMSEN-1615-Assert error: Test case is failed because MS is H323 registered!" #Online
    





