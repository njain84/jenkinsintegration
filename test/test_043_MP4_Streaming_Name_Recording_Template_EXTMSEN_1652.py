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

class Two_streamings_names(unittest.TestCase):


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
            time.sleep(2)
            call_to_MS = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
            call_to_MS.EPSIPcall()
            time.sleep(2)
            myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), driver)
            # login the admin portal
            myloginadmin.doLoginadmin()
            driver.implicitly_wait(50)
            stream_name=driver.find_element_by_xpath("//*[@id='call-table-row-0']/td[9]").text
            print('Stream name is',stream_name)
            Value_stream = stream_name.split()
            final_names = []
            i = 0
            for i in range(0,6):
                if Value_stream[i] == 'Stream1':
                    print('final stream is:',Value_stream[i])
                    final_names.append(Value_stream[i])


                elif Value_stream[i] == 'Stream2':
                    print('final stream is:', Value_stream[i])
                    final_names.append(Value_stream[i])
                i = i+1

            final_names.sort()

            print('final_names', final_names)
            required_value1 = 'Stream1'
            required_value2 = 'Stream2'
            assert final_names[0] == required_value1, 'Test case is failed because name are not Stream1 or Stream2'
            assert final_names[1] == required_value2, 'Test case is failed because name are not Stream1 or Stream2'
        finally:
            print('Done')
            driver.quit()
            Hang_up_call = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            Hang_up_call.doepcallhangup()
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            My_Template.disable_one_live_stream()

    













