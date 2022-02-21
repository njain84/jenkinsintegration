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
from test import test_044_Login_with_Default_Password_EXTMSEN_1542




class Regression(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1542', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1652')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    
        
    def test_EXTMSEN_1542(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_044_Login_with_Default_Password_EXTMSEN_1542.default_password
        Regression.test_login_with_default_password(self)

    #if __name__ == '__main__':
        #unittest.main()
