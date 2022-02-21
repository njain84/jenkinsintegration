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
from .POM.EPlogin_call import Eplogin
from configparser import ConfigParser
from .POM.EPlogin_callhangup import Ephangup

class admin_tcp_SIP_Call_without_DMA(unittest.TestCase):

    def test_admin_tcp_SIP_Call(self):

        
        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')#options=options
        parser = ConfigParser()
        parser.read('config.ini')


        try:
            print("Hello....")
           
            #unregister the EP
            unregister = Eplogin(parser.get('bug_tracker', 'epurl'),self.driver)
            unregister.Only_unregister_EP()
            # it will set the protocol of MS as tcp but it will not be register.
            run = admin_Registration(self.driver)
            actualprotocolvaue = run.admin_registration_tcp_check()
            print('protocol value is:',actualprotocolvaue)
            # MS will call to EP thru admin portal
            call = admin_call(self.driver)
            actualresult = call.admin_dialouttorecord()
            print('output is', actualresult)
            
            
            
            # it is created time >= call start time
            assert actualresult[0] >= actualresult[1], "EXTMSEN-1611-Assert error: file is not created"
            assert 'SIP' == actualresult[2], "EXTMSEN-1611_Test case is failed because protocol is not SIP!"
            assert actualprotocolvaue == '1', "EXTMSEN-1611-Protocol is not tcp"


        finally:
            # it will register the EP again with GK.
            register = Eplogin(parser.get('bug_tracker', 'epurl'),self.driver)
            register.EP_SIP_registration()
            print('finally')
            Epdisconnect= Ephangup(parser.get('bug_tracker', 'epurl'),self.driver)
            Epdisconnect.doepcallhangup()









