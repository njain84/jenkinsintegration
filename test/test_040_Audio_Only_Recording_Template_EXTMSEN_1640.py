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
from .POM.EPlogin_callhangup import Ephangup
from .POM.POM_admin_template import admin_Template
from .POM.POM_admin_call_dial_in_out import admin_call

class Audio_Only_call(unittest.TestCase):

    def test_Audio_only(self):

        
        try:
            
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            time.sleep(2)
            print('Now template')
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            My_Template.Audio_only()
            time.sleep(2)
            start_Sip_call = admin_call(driver)
            actual_Live_info = start_Sip_call.admin_dialouttorecord()
            print('actual_Live_info :', actual_Live_info[5])
            print('Created time and call start time', actual_Live_info[0], actual_Live_info[1])
            Live_info = '64kbps[M4A]'
            assert actual_Live_info[5] == Live_info,'EXTMSEN-1640-Assert error:Call is not Audio only'
            assert actual_Live_info[0] >= actual_Live_info[1],'EXTMSEN-1640-Assert error:file is not created'
            time.sleep(5)
        finally:
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            time.sleep(2)
            call_hangup = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            call_hangup.doepcallhangup()
            time.sleep(2)
            print('Now template')
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            My_Template.Audio_only()
            time.sleep(1)
            My_Template.enable_Live()

            driver.close()





