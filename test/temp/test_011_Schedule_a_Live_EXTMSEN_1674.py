import time
import logging
from selenium import webdriver
from test import test_012_Schedule_a_Live_EXTMSEN_1674
import pyautogui
from Login_config.LoginHandleradminportal import Loginmsadmin
from configparser import ConfigParser
import unittest
import openpyxl
import allure
import pytest
from configparser import ConfigParser
from Login_config.LoginHandler import Loginms
from datetime import datetime
from datetime import datetime as dt


class Smoke(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1674', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN-1674')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))


    def test_EXTMSEN_1674(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_012_Schedule_a_Live_EXTMSEN_1674.Schedulelive
        smoke1.test_schedule_live(self)

        if __name__ == '__main__':
            unittest.main()

