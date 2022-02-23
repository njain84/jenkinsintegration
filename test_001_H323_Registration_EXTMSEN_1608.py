import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
import openpyxl
from configparser import ConfigParser
import pytest
from selenium.common.exceptions import TimeoutException, WebDriverException


class H323(unittest.TestCase):

    def test_H323_Registration(self):

        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')

        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
		
        #print("do login Method called :", self.username)
        self.driver.get('http://10.97.52.56/admin/login.jsf')
        time.sleep(5)
        print("Hi")
        self.driver.find_element_by_id('loginForm:userName').send_keys(admin)
        print("Hi")
        time.sleep(3)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys(123)
        print(self.driver.find_elements_by_class_name('btn')[0])
        time.sleep(5)
        self.driver.find_elements_by_class_name('btn')[1].click()
        print(self.driver.find_elements_by_id('dialOutButton'))

    if __name__ == '__main__':
        unittest.main()
