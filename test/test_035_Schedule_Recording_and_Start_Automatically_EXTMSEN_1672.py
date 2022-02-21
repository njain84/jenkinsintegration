import unittest
import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
from .POM.Event_tab import event_tab_Schedule_Recording
import pytest
from .POM.EPlogin_call import Eplogin
from .POM.EPlogin_callhangup import Ephangup

class Schedule_and_start_recording_automatically(unittest.TestCase):


    def test_Schedule_and_start_recording_automatically(self):


        
        parser = ConfigParser()
        parser = ConfigParser()
        parser.read('config.ini')

        try:

            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')

            EPlogin = Eplogin(parser.get('bug_tracker', 'epurl'), driver)
            # login the EP
            EPlogin.doepLogin()
            time.sleep(2)
            Schedule_event = event_tab_Schedule_Recording(driver)
            Schedule_event.test_event_Schedule_Recording()
            Schedule_event.test_Auto_start_recording()
            final_call_status = Schedule_event.test_final_scheddule_recording_result()
            time.sleep(50)
            Schedule_event.test_Stop_event()
            time.sleep(2)
            EPcallHang_up = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            EPcallHang_up.doepcallhangup()
            assert 'Hang up' == final_call_status,"EXTMSEN-1672-Assert error: Call has not started"
            
            
        finally:

            try:
                print('This is always executed')
                
                driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
                parser = ConfigParser()
                parser.read('config.ini')
                ephangup = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
                ephangup.doepcallhangup()
                driver.close()
                

            except WebDriverException as e:
                print('Result:', e)
                
            
            
            
            

        

    
    



