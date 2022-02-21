import webbrowser
import requests
import tkinter as tk
import time
import logging
from test import test_007_RMX_Recording_Links_Dialin_SIP_EXTMSEN_1629
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
import unittest

from datetime import datetime
import openpyxl
import pyautogui
from configparser import ConfigParser
import allure
import pytest



class Smoke(unittest.TestCase):
    parser = ConfigParser()
    parser.read('config.ini')
    TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1629', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1629')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    def test_EXTMSEN_1629(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_007_RMX_Recording_Links_Dialin_SIP_EXTMSEN_1629.Dialoutrecordinglink
        smoke1.test_dialoutfromRMX(self)


if __name__ == '__main__':
    unittest.main()



