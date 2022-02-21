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
from test import test_037_Max_call_rates_Max_Resolution_Recording_Template_EXTMSEN_1639




class Regression(unittest.TestCase):


    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN_1639', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1612')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1612(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_037_Max_call_rates_Max_Resolution_Recording_Template_EXTMSEN_1639.Max_call_rate_Sip_H323_call
        Regression.test_EXTMSEN_1639(self)

    #if __name__ == '__main__':
        #unittest.main()
