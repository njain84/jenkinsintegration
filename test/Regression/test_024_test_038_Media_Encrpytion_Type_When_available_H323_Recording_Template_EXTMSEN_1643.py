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
from test import test_038_Media_Encrpytion_type_When_available_H323_Recording_Template_EXTMSEN_1643




class Regression(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1643', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1643')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1643(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_038_Media_Encrpytion_type_When_available_H323_Recording_Template_EXTMSEN_1643.AES_in_H323_call
        Regression.test_AES_H323_call(self)

    #if __name__ == '__main__':
        #unittest.main()
