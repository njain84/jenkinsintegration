import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
import unittest
import datetime
import openpyxl
from configparser import ConfigParser
import pytest
from test import test_003_Registration_with_UDP_EXTMSEN_1606
import allure


class Smoke(unittest.TestCase):
    
    parser = ConfigParser()
    parser.read('config.ini')
    TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1606', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1608')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    def test_EXTMSEN_1606(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_003_Registration_with_UDP_EXTMSEN_1606.Temp
        smoke1.test_UDP_Registration(self)

if __name__ == '__main__':
    unittest.main()


