import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
import unittest
from datetime import datetime
from configparser import ConfigParser
import openpyxl
import allure
import pytest
from test import test_047_Verify_that_media_suite_can_be_synchronise_with_NTP_server_EXTMSEN_1552




class Regression(unittest.TestCase):

    parser = ConfigParser()
    configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
    parser.read(configFilePath)
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1522', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1522')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1522(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_047_Verify_that_media_suite_can_be_synchronise_with_NTP_server_EXTMSEN_1552.MS_with_NTP_server
        Regression.test_NTP_Server(self)

    #if __name__ == '__main__':
        #unittest.main()
