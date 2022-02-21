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
from test import test_058_Testsurvey_Create_a_Private_Test_with_viewer_EXTMSEN_1704




class Regression(unittest.TestCase):


    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1704', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1704')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1704(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_058_Testsurvey_Create_a_Private_Test_with_viewer_EXTMSEN_1704.private_test
        Regression.test_private_test_EXTMSEN_1704(self)

    #if __name__ == '__main__':
        #unittest.main()
