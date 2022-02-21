import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
from .POM.POM_Registration import admin_Registration
from .POM.EPlogin_call import Eplogin
from .POM.EPlogin_callhangup import Ephangup
import unittest
from .POM.POM_admin_call_dial_in_out import admin_call
# Scenerio is for without DMA call

class admin_tcp_dialin_call_without_DMA(unittest.TestCase):

    def test_SIP_TCP_Dialin_call(self):
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        parser = ConfigParser()
        parser.read('config.ini')
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            print("Hello....")

            # tcp will be setting up
            tcp_protocol_setting = admin_Registration(driver)
            actualprotocolvalue = tcp_protocol_setting.admin_registration_tcp_check()
            print('Value is:',actualprotocolvalue)
            #Ep unrigistration with GK
            Unregister_EP = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
            Unregister_EP.Only_unregister_EP()
            # EP will call to MS
            EPcalltoMS = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
            callstart_time = EPcalltoMS.call_to_MSIP()
            print('call started at:',callstart_time)
            # MS will check the call etc. inside MS
            MS_DialIN = admin_call(driver)
            actualresult = MS_DialIN.admin_dialin()
            print('returned protocol is:',actualresult[1])
            # actualresult[0] is mediafile creation time and callstart_time is when Ep dialed the call to MS
            assert actualresult[0] >= callstart_time, "EXTMSEN-1613-Assert error: file is not created"
            assert 'SIP' == actualresult[1], "EXTMSEN-1613_Test case is failed because protocol is not SIP!"
            assert actualprotocolvalue == '1', "EXTMSEN-1613_Test case is failed because transport protocol is not TCP!"
            

        finally:
        
            #It will register the EP
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            EPRegistration = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
            EPRegistration.EP_SIP_registration()
            try:
                print('This is always executed')
                ephangup = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
                ephangup.doepcallhangup()

            except WebDriverException as e:
                print('Result:', e)
                
        driver.quit()










