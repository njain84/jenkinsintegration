import unittest
import webbrowser
from datetime import datetime
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
from Login_config.LoginHandleradminportal import Loginmsadmin
import pytest
from .POM.POM_admin_template import admin_Template
from .POM.POM_admin_call_dial_in_out import admin_call
from .POM.EPlogin_call import Eplogin
from .POM.EPlogin_callhangup import Ephangup
from .POM.Event_tab import event_tab_Schedule_Recording

class Two_streamings(unittest.TestCase):


    def test_Two_streamings(self):


        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        try:
            time.sleep(2)
            print('Now template')
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            My_Template.two_live_streaming()
            print('template done')
            
            time.sleep(5)
            
            call_to_MS = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
            call_to_MS.EPSIPcall()
            time.sleep(2)
            event = event_tab_Schedule_Recording(driver)
            event.Navigate_to_event()
            # It will click on setting option
            print('joined')
            time.sleep(12)
            driver.find_element_by_id('dropdown_setting').click()
            # It will fetch the value of resolution
            time.sleep(2)
            value1 = driver.find_element_by_xpath('//*[@id="unicastDiv"]/div[3]/ul/li[1]/span').text
            print('value1 is', value1)
            actual_value1 = value1.split(' ')
            print('actual_value1 is', actual_value1[1])
            value2 = driver.find_element_by_xpath('//*[@id="unicastDiv"]/div[3]/ul/li[2]/span').text
            print('value2 is', value2)
            actual_value2 = value2.split(' ')
            print('actual_value2 is', actual_value2[1])
            required_value1 = '(320Kbps)'
            required_value2 = '(384Kbps)'
            time.sleep(2)
            Hang_up_call = Ephangup(parser.get('bug_tracker', 'epurl'),driver)
            Hang_up_call.doepcallhangup()

            assert actual_value1[1] == required_value1 or required_value2, "EXTMSEN-1651-Assert error:Resolution is not correct"
            assert actual_value2[1] == required_value2 or required_value1, "EXTMSEN-1651-Assert error:Dual stream is not available"
        finally:
            print('Done')
            driver.quit()
            Hang_up_call = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            Hang_up_call.doepcallhangup()

    













