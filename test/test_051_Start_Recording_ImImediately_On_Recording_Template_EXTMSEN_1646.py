import time
import unittest
from .POM.POM_admin_template import admin_Template
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from configparser import ConfigParser
from .POM.POM_admin_call_dial_in_out import admin_call

class Recording_immediately(unittest.TestCase):

    def test_recording(self):

        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        try:
            My_template = admin_Template(driver)
            My_template.Recording_Template()
            driver.implicitly_wait(2)
            My_template.Archiving()
            driver.implicitly_wait(2)
            My_template.start_recording_immidiately()
            UDP_call = admin_call(driver)
            time_output = UDP_call.admin_dialouttorecord()
            assert time_output[0] < time_output[1], 'Test case is Failed because archive has been created'

        finally:
            My_template = admin_Template(driver)
            My_template.Recording_Template()
            driver.implicitly_wait(2)
            My_template.Archiving()
            time.sleep(2)
            driver.implicitly_wait(2)
            My_template.start_recording_immidiately()

        admin_login = Loginmsadmin('admin', '123', parser.get('bug_tracker', 'url'), driver=driver)
        admin_login.doLoginadmin()
        time.sleep(2)
        UDP_call = admin_call(driver)
        time_output_new = UDP_call.admin_dialouttorecord()
        assert time_output_new[0] >= time_output_new[1], 'Test case is Failed because archive has not been created'




