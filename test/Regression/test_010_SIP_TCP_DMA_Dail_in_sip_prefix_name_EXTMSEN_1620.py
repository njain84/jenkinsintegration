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
from test import test_020_SIP_TCP_DMA_Dail_in_sip_prefix_name_EXTMSEN_1620


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1620', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1619')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1620(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_020_SIP_TCP_DMA_Dail_in_sip_prefix_name_EXTMSEN_1620.testdialindmaformep
        Regression.test_dial_in_dma_MS_sip_tcp_form_ep(self)

    if __name__ == '__main__':
        unittest.main()
