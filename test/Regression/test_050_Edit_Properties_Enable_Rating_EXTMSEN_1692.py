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
from test import test_050_Edit_Properties_Enable_Rating_EXTMSEN_1692




class Regression(unittest.TestCase):

    parser = ConfigParser()
    configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
    parser.read(configFilePath)
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1692', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1692')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))
    

    
        
    def test_EXTMSEN_1699(self):
        
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_050_Edit_Properties_Enable_Rating_EXTMSEN_1692.rating_like_dislike
        Regression.test_Rating(self)

    #if __name__ == '__main__':
        #unittest.main()
