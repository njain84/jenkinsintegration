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
from test import test_039_Media_Encrpytion_Type_When_available_SIP_TLS_Recording_Template_EXTMSEN_1644


class Regression(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1644', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1644')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1644(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_039_Media_Encrpytion_Type_When_available_SIP_TLS_Recording_Template_EXTMSEN_1644.AES
        Regression.test_AES(self)

    #if __name__ == '__main__':
        #unittest.main()
