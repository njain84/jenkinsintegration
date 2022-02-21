from configparser import ConfigParser
from datetime import datetime

from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium import webdriver
from pywinauto.application import Application
import time
from .POM.POM_admin_template import admin_Template
import unittest
from Login_config.LoginHandleradminportal import Loginmsadmin
from .POM.configuration_tab import config_server
from selenium.webdriver.common.keys import Keys

class MS_with_NTP_server(unittest.TestCase):


    def test_NTP_Server(self):

        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        my_server = config_server()
        # it will login MS and click to configuration
        my_server.click_config()
        time.sleep(1)
        my_server.click_System_time()
        # it will click to Ntp_server
        time.sleep(1)
        my_server.Configure_NTP_server()
        time.sleep(180)
        my_server.click_config()
        time.sleep(1)
        my_server.click_System_time()
        actual_time = my_server.NTP_server_current_time()
        print('Actual time is',actual_time)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # Below code will split the time and calculate it in seconds
        actual_second = actual_time.split(':')
        current_second = current_time.split(':')
        Asec = int(actual_second[0])*3600 + int(actual_second[1])*60 + int(actual_second[2])
        Csec = int(current_second[0])*3600 + int(current_second[1])*60 + int(current_second[2])
        print('Asec :',Asec)
        print('Csec :', Csec)
        print('difference is',abs(int(Asec) - int(Csec)))
        if abs(int(Asec) - int(Csec)) == 1:
            actual_time = current_time

        print('Current time is',current_time)

        assert actual_time == current_time,f'test case EXTMSEN-1552 is failed because {actual_time} is not same as {current_time}'


    if __name__ == '__main__':
        unittest.main()

