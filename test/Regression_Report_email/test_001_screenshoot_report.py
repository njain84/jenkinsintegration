import os
from selenium import webdriver
import webbrowser
import pyautogui
import time
#from PIL import ImageGrab
from test import test_screenshoot_report_Regression
import base64
# it will take screen shot of first page of report
import unittest
import pytest
import allure


class Screen1(unittest.TestCase):

    def test_screenshot1(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        screen1 = test_screenshoot_report_Regression.Screen
        screen1.test_screenshot(self)

    if __name__ == '__main__':
        unittest.main()
