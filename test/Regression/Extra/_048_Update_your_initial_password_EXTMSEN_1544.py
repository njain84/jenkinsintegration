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
from test import test_045_Update_your_initial_password_EXTMSEN_1544




class Regression(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1544', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1544')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    
        
    def test_EXTMSEN_1544(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_045_Update_your_initial_password_EXTMSEN_1544.update_default_password
        Regression.test_update_default_password(self)

    #if __name__ == '__main__':
        #unittest.main()
