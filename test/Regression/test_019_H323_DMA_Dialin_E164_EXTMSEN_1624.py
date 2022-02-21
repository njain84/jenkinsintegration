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
from test import test_013_H323_DMA_Dial_in_E164_EXTMSEN_1624


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1628', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1624')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1624(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_013_H323_DMA_Dial_in_E164_EXTMSEN_1624.testdialindmah323callformep
        Regression.test_dial_in_dma_MS_H323_form_ep(self)

    if __name__ == '__main__':
        unittest.main()
