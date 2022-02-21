import unittest
import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
from .POM.POM_My_media_center import My_Meida_Center
from .POM.POM_My_media_center import Admin

class closed_caption(unittest.TestCase):

    def test_closed_caption(self):
        print("Hello....")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)
        Myuserportallogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'),self.driver)
        Myuserportallogin.doLogin()
        time.sleep(4)
        Media_center = My_Meida_Center(self.driver)
        Media_center.Click_My_Media_Center()
        time.sleep(3)
        My_center_Admin = Admin(self.driver)
        cielo_configuration = My_center_Admin.third_party_integration()
        time.sleep(2)
        Media_center = My_Meida_Center(self.driver)
        Media_center.Click_My_Media_Center()
        time.sleep(2)
        VoD_caption_Result = Media_center.VoD_closed_caption()
        assert VoD_caption_Result == 'In progress.', "EXTMSEN-1815-Assert error: VoD has not been upoaded in cielo24"
        assert cielo_configuration == 'Tested successfully.', "EXTMSEN-1815-Assert error: Cielo 24 is not configured"


        time.sleep(10)








