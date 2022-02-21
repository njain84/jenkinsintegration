import time
import logging
from selenium import webdriver
import pyautogui
from Login_config.LoginHandleradminportal import Loginmsadmin
from configparser import ConfigParser
import unittest
import openpyxl
from test import test_002_system_upgrade
import allure

class system_upgrade(unittest.TestCase):

    def test_upgrade(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        upgrade = test_002_system_upgrade.System_upgrade
        upgrade.test_System_upgrade(self)

    if __name__ == '__main__':
        unittest.main()
