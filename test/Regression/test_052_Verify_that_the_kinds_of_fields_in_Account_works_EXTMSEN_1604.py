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
from test import test_054_Verify_that_the_kinds_of_fields_in_Account_works_EXTMSEN_1604




class Regression(unittest.TestCase):


    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1604', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1604')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1604(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_054_Verify_that_the_kinds_of_fields_in_Account_works_EXTMSEN_1604.Accounts_verification
        Regression.test_Accounts_verification(self)

    #if __name__ == '__main__':
        #unittest.main()
