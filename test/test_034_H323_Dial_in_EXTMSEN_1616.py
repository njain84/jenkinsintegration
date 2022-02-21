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
from .POM.EPlogin_call import Eplogin


class admin_H323_dial_IN_withoutdma(unittest.TestCase):

    def test_H323_dial_IN_withoutdma(self):
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        time.sleep(2)
        registration = admin_Registration(driver)
        registration_status = registration.test_H323_unregister()
        print('Protocol is', registration_status)
        time.sleep(2)
        EPcall_to_MS = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
        Call_start_time = EPcall_to_MS.EP_to_MS_H323_IP_call()
        print('Call started:', Call_start_time)
        time.sleep(2)
        Dial_in_call = admin_call(driver)
        funtion_values = Dial_in_call.admin_dialin()
        print('values are:', funtion_values)
        driver.close()
        assert funtion_values[0] >= Call_start_time, "EXTMSEN-1616-Assert error: Test case is failed because file is not created!"
        assert funtion_values[1] == "H323", "EXTMSEN-1616-Assert error: Test case is failed because protocol is not H323!"
        assert registration_status != 'Online', "EXTMSEN-1616-Assert error: Test case is failed because MS is H323 registered!"  # Online
