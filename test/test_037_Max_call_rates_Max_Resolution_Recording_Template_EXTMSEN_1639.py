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
from .POM.Event_tab import event_tab_Schedule_Recording
from Login_config.LoginHandleradminportal import Loginmsadmin
import pytest
from .POM.POM_admin_template import admin_Template
from .POM.POM_admin_call_dial_in_out import admin_call
from .POM.EPlogin_callhangup import Ephangup
from .POM.EPlogin_call import Eplogin

class Max_call_rate_Sip_H323_call():

    

    def test_EXTMSEN_1639(self):

        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        
        try:
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            #unregister the EP
            unregister = Eplogin(parser.get('bug_tracker', 'epurl'),self.driver)
            unregister.Only_unregister_EP()
            time.sleep(5)
            myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
            # login the admin portal
            myloginadmin.doLoginadmin()
            time.sleep(2)
            print('Now template')
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            My_Template.Call_rate()
            time.sleep(2)
            H323_SIP_call = admin_call('driver')
            H323_actual_call_rate_archive = H323_SIP_call.admin_dialouttorecord_H323()
            print('actual H323_call rate is:', H323_actual_call_rate_archive[3])
            H323_SIP_excepted_call_rate = '4000'
            SIP_actual_call_rate_archive = H323_SIP_call.admin_dialouttorecord()
            print('actual SIP_call rate is:', SIP_actual_call_rate_archive)
            assert H323_actual_call_rate_archive[3] >= H323_SIP_excepted_call_rate, "EXTMSEN-1639-Assert error:H323 call rate is less then 4000"
            assert H323_actual_call_rate_archive[0] >= H323_actual_call_rate_archive[1], "EXTMSEN-1639-Assert error:File is not created in H323 call"
            assert SIP_actual_call_rate_archive[0] >= SIP_actual_call_rate_archive[1], "EXTMSEN-1639-Assert error:File is not created in SIP call"
            assert SIP_actual_call_rate_archive[4] >= H323_SIP_excepted_call_rate, "EXTMSEN-1639-Assert error:SIP call rate is less then 4000"
            
        finally:
            time.sleep(4)
            # it will register the EP again with GK.
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            EPRegistration = Eplogin(parser.get('bug_tracker', 'epurl'),driver)
            EPRegistration.EP_SIP_registration()
            time.sleep(4)
            #it will disconnect the call from Ep if there
            Epdisconnect= Ephangup(parser.get('bug_tracker', 'epurl'),self.driver)
            Epdisconnect.doepcallhangup()            
            self.driver.close()

            
        






