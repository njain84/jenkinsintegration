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
from test import test_031_Closed_Caption_3rdparty_integration_EXTMSEN_1815




class Regression(unittest.TestCase):


    parser = ConfigParser()
    configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
    parser.read(configFilePath)
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1815', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN-1815')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1815(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_031_Closed_Caption_3rdparty_integration_EXTMSEN_1815.closed_caption
        Regression.test_closed_caption(self)

    #if __name__ == '__main__':
        #unittest.main()
