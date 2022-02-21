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
import unittest
from datetime import datetime
from configparser import ConfigParser
import openpyxl
import allure
import pytest
from test import test_005_RMX_Dialout_conference_H323_EXTMSEN_1628 


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1628', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1628')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1608(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_005_RMX_Dialout_conference_H323_EXTMSEN_1628.Dialtoephh323vmr
        smoke1.test_dial_out_h323_conference(self)

    if __name__ == '__main__':
        unittest.main()