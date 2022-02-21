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
from test import test_014_H323_DMA_Dial_out_EXTMSEN_1623


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1623', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1623')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1623(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_014_H323_DMA_Dial_out_EXTMSEN_1623.DialtoepH323
        Regression.test_H323_mstoep_call(self)

    if __name__ == '__main__':
        unittest.main()
