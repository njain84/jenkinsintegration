import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
import unittest
from datetime import datetime
import openpyxl
from openpyxl import Workbook
from test import test_002_Dail_to_record_H323_call_adminportal_EXTMSEN_1625
import pytest
import allure

class Smoketest(unittest.TestCase):
    
    parser = ConfigParser()
    parser.read('config.ini')
    TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1625', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1625')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    def test_EXTMSEN_1625(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_002_Dail_to_record_H323_call_adminportal_EXTMSEN_1625.Dialtoeph323
        smoke1.test_h323_p2p_call(self)
    


if __name__ == '__main__':
    unittest.main()




