import unittest
from selenium import webdriver
import webbrowser
from test import test_009_SIP_Registration_TLS_EXTMSEN_1607
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser

import allure
import pytest


class Smoketest(unittest.TestCase):

    parser = ConfigParser()
    parser.read('config.ini')
    TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'

    @allure.issue("140", parser.get('bug_tracker', 'build'))
    @allure.link('https://jira.harman.com/jira/browse/EXTMSEN-1607', name='Jira_Click me once')
    @allure.title('JiraID-EXTMSEN_1607')
    @allure.description("Execution is on" + parser.get('bug_tracker', 'build'))

    def test_EXTMSEN_1607(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_009_SIP_Registration_TLS_EXTMSEN_1607.TLS
        smoke1.test_TLS_registration(self)


if __name__ == '__main__':
    unittest.main()