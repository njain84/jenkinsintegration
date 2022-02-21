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
from test import test_048_Create_a_Public_Channel_EXTMSEN_1698




class Regression(unittest.TestCase):

    parser = ConfigParser()
    configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
    parser.read(configFilePath)
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1698', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1698')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1698(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_048_Create_a_Public_Channel_EXTMSEN_1698.create_a_public_channel
        Regression.test_public_channel(self)

    #if __name__ == '__main__':
        #unittest.main()
