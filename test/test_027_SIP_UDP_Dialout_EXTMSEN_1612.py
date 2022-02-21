import time
import logging
from selenium import webdriver
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
from .POM.POM_Registration import admin_Registration
from .POM.POM_admin_call_dial_in_out import admin_call
from configparser import ConfigParser
from .POM.EPlogin_callhangup import Ephangup
from .POM.EPlogin_call import Eplogin

class admin_UDP_SIP_Call_without_DMA(unittest.TestCase):

    def test_admin_UDP_SIP_Call(self):

        parser = ConfigParser()
        parser.read('config.ini')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)


        try:
            print("Hello....")
            #unregister the EP
            unregister = Eplogin(parser.get('bug_tracker', 'epurl'),self.driver)
            unregister.Only_unregister_EP()
            time.sleep(5)
            #select the UDP withpout registration with DMA
            run = admin_Registration(self.driver)
            run.admin_registration_udp_check()
            call = admin_call(self.driver)
            actualresult = call.admin_dialouttorecord()
            print('output is', actualresult)
            # created time >= call start time
            assert actualresult[0] >= actualresult[1], "EXTMSEN-1612-Assert error: file is not created"
            assert 'SIP' == actualresult[2], "EXTMSEN-1612_Test case is failed because protocol is not SIP!"


        finally:
            time.sleep(4)
            # it will register the EP again with GK.
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            #it will disconnect the call from Ep if there
            Epdisconnect= Ephangup(parser.get('bug_tracker', 'epurl'),self.driver)
            Epdisconnect.doepcallhangup()
            time.sleep(4)
            EPRegistration = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
            EPRegistration.EP_SIP_registration()
            
            








