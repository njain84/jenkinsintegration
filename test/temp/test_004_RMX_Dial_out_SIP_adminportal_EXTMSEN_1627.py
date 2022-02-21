import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
import sys
import os

from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
import unittest
from datetime import datetime

import openpyxl
from test import test_004_RMX_Dial_out_SIP_adminportal_EXTMSEN_1627
import allure
import pytest
#from Login_config.EPlogin_call import Eplogin

class Smoke(unittest.TestCase):
    parser = ConfigParser()
    parser.read('config.ini')
    EST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1627', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1627')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    def test_EXTMSEN_1627(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_004_RMX_Dial_out_SIP_adminportal_EXTMSEN_1627.Dialtoephsipvmr
        smoke1.test_sip_vmr_call(self)


if __name__ == '__main__':
    unittest.main()
