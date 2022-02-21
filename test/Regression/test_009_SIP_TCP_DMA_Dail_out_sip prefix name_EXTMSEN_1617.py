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
from test import test_033_SIP_TCP_DMA_Dail_out_sip_prefix_name_EXTMSEN_1617


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1617', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1617')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1617(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_033_SIP_TCP_DMA_Dail_out_sip_prefix_name_EXTMSEN_1617.Dialtoepsip_prefixname
        Regression.test_dial_out_TCP_SIP_EP_Prefixname(self)

    if __name__ == '__main__':
        unittest.main()
