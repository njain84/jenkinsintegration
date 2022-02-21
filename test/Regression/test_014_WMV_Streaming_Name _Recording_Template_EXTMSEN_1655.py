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
from test import test_046_WMV_Streaming_Name_Recording_Template_EXTMSEN_1655


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read(r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1655', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1655')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1655(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        Regression = test_046_WMV_Streaming_Name_Recording_Template_EXTMSEN_1655.WMV_streaming
        Regression.test_wmv_streaming(self)

    if __name__ == '__main__':
        unittest.main()
