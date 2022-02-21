from configparser import ConfigParser
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium import webdriver
from pywinauto.application import Application
import time
from .POM.POM_admin_template import admin_Template
import unittest
from .POM.EPlogin_call import Eplogin
from .POM.EPlogin_callhangup import Ephangup
from .POM.POM_admin_call_dial_in_out import admin_call

class H264_High_Profile(unittest.TestCase):

    def test_H264_high_profile(self):

        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        try:
            My_template = admin_Template(driver)
            My_template.Recording_Template()
            My_template.click_on_Live_streaming_MP4()
            My_template.enable_H264_High_profile()
            time.sleep(5)
            # MS will call to EP
            call = admin_call(driver)
            call = admin_call(driver)
            call_result = call.admin_dialouttorecord()
            assert call_result[7]=='H264-HP','Test case is failed as it is not high profile'
            #createdtime >= dt_string
            assert call_result[0] >= call_result[1], "EXTMSEN-1627-Assert error: file is not created"


        finally:

            Hang_up_call = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            Hang_up_call.doepcallhangup()

