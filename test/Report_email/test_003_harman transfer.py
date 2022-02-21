import time
import logging
from selenium import webdriver
from test import test_003_harman_transfer
import webbrowser
import openpyxl
from pywinauto.application import Application
import pyautogui
from configparser import ConfigParser
import unittest
import time
import allure
import pytest



class Transfer(unittest.TestCase):

    def test_Harman_transfer1(self):
        self.launch_site()

    @allure.step("Launch1 site")

    def launch_site(self):
        transfer = test_003_harman_transfer.Transfer_harman
        transfer.test_report_transfer(self)


    if __name__ == '__main__':
        unittest.main()
