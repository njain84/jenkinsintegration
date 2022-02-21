import unittest
import webbrowser
from datetime import datetime

import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
from .POM.Event_tab import event_tab_Schedule_Recording
from Login_config.LoginHandleradminportal import Loginmsadmin
import pytest
from .POM.EPlogin_call import Eplogin
from .POM.EPlogin_callhangup import Ephangup


class Schedule_and_start_and_end_recording_automatically(unittest.TestCase):

    def test_Schedule_and_start_and_end_recording_automatically(self):

        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')

        try:
            #driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            EPlogin = Eplogin(parser.get('bug_tracker', 'epurl'), driver)
            # login the EP
            EPlogin.doepLogin()
            Schedule_event = event_tab_Schedule_Recording(driver)
            Schedule_event.test_event_Schedule_Recording()
            now = datetime.now()
            dt_string = now.strftime("%m-%d-%Y %I:%M%p" + ' (GMT+05:30)')
            print('Current time', dt_string)
            Schedule_event.test_Auto_start_recording()
            Schedule_event.test_End_Automatically_call()
            final_call_status = Schedule_event.test_final_scheddule_recording_result()
            time.sleep(1000)
            # it will verify the call duration and call
            myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), driver)
            # login the admin portal
            myloginadmin.doLoginadmin()
            time.sleep(100)  # Now it will go to Archive and check the file
            driver.find_element_by_id('a_1002').click()
            time.sleep(1)
            driver.find_element_by_id('a_1003').click()
            time.sleep(4)
            createdtime = driver.find_element_by_xpath("//*[@id='archive-table-row-0']/td[4]").text
            print('time is', createdtime)
            time.sleep(2)

            actual_duration = driver.find_element_by_xpath("// *[ @ id = 'archive-table-row-0'] / td[5]").text
            print('Actual_Duration:', actual_duration)
            duration = '00:14:00'
            duration1 = '00:15:30'
            time.sleep(2)
            EPcallHang_up = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            EPcallHang_up.doepcallhangup()

            # Schedule_event.test_Stop_event()
            assert createdtime >= dt_string, "EXTMSEN-1673-Assert error:file is not created"
            assert duration <= actual_duration <= duration1, "EXTMSEN-1673-call has been disconnected early"
            assert 'Hang up' == final_call_status, "EXTMSEN-1673-Assert error: Call has not started"

        finally:
            try:
                parser = ConfigParser()
                configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
                parser.read(configFilePath)
                EPcallHang_up = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
                EPcallHang_up.doepcallhangup()
            except WebDriverException as e:
                print('Ep is already disconnected:', e)
            driver.close()








