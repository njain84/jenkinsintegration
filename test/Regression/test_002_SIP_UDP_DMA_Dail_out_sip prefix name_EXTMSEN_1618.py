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
from test import test_016_SIP_UDP_DMA_Dail_out_sip_prefixname_EXTMSEN_1618


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1618', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1619')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1618(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_016_SIP_UDP_DMA_Dail_out_sip_prefixname_EXTMSEN_1618.Dialtoepsip_UDP_prefixname
        Regression.test_dial_out_SIP_UDP_EP_Prefixname(self)

    if __name__ == '__main__':
        unittest.main()
