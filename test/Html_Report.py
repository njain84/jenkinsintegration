import unittest
from selenium import webdriver
import webbrowser
import test_001_H323_Registration_EXTMSEN_1608
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
import pytest


class Smoketest(unittest.TestCase):

    def test_EXTMSEN_1608(self):
        self.launch_site()


    @allure.step("Launch1 site")
    def launch_site(self):
        smoke1 = test_001_H323_Registration_EXTMSEN_1608.H323
        smoke1.test_H323_Registration(self)


if __name__ == '__main__':
    unittest.main()