import time
import logging
from selenium import webdriver
import pyautogui
from Login_config.LoginHandleradminportal import Loginmsadmin
from configparser import ConfigParser
import unittest
import openpyxl
import allure
import pytest
from configparser import ConfigParser
from test import test_011_fallback_after_upgrade_EXTMSEN_1553

class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1553', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN-1553')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1553(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_011_fallback_after_upgrade_EXTMSEN_1553.System_Fallback_upgrade
        smoke1.test_fallback_upgrade(self)

        if __name__ == '__main__':
            unittest.main()

