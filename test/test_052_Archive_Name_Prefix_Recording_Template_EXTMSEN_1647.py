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

class file_prefix(unittest.TestCase):

    def test_file_prefix(self):

        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)

        try:
            time.sleep(2)
            print('Now template')
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            My_Template.Archiving()
            My_Template.Archive_Name_Prefix()
            # It will call to EP
            call = admin_call(driver)
            call_result = call.admin_dialouttorecord()
            print(call_result[6])
            Excepted = True
            assert Excepted == call_result[6],'Test is failed EXTMSEN-6812 as name of file is not as excepted'

        finally:
            print('done')
            Hang_up_call = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            Hang_up_call.doepcallhangup()

    if __name__ == '__main__':
        unittest.main()




