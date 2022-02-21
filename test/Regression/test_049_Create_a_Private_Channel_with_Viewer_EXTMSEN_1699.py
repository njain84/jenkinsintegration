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
from test import test_049_Create_a_Private_Channel_with_Viewer_EXTMSEN_1699




class Regression(unittest.TestCase):

    parser = ConfigParser()
    configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
    parser.read(configFilePath)
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1699', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1699')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1699(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_049_Create_a_Private_Channel_with_Viewer_EXTMSEN_1699.create_a_private_channel
        Regression.test_private_channel(self)

    #if __name__ == '__main__':
        #unittest.main()
