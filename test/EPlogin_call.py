import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
import openpyxl
from configparser import ConfigParser


class Eplogin:

    def __init__(self, url: str, driver):
        print("Constructor of End point Login Handler")
        self.url = url
        self.driver = driver

    def doepLogin(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        time.sleep(20)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        time.sleep(10)
        self.driver.find_element_by_id('textfield-1061-inputEl').send_keys(
            parser.get('bug_tracker', 'vmr'))  # Entering the dialing number
        time.sleep(5)
        self.driver.find_element_by_id('button-1062-btnIconEl').click()  # click on call
        time.sleep(5)
        print("step----------------------1")
        # self.driver.find_element_by_id('splitbutton - 1040 - btnIconEl').click()     #  hangup the call



    def EPSIPcall(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        time.sleep(20)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        time.sleep(10)
        self.driver.find_element_by_id('textfield-1061-inputEl').send_keys(parser.get('bug_tracker', 'mssipaddress'))  # Entering the dialing number
        time.sleep(5)
        self.driver.find_element_by_id('button-1062-btnIconEl').click()  # click on call
        time.sleep(5)
        print("step----------------------1")
    def EPH323call(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        time.sleep(20)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        time.sleep(10)
        self.driver.find_element_by_id('textfield-1061-inputEl').send_keys(parser.get('bug_tracker', 'msh323address'))  # Entering the dialing number
        time.sleep(5)
        self.driver.find_element_by_id('button-1062-btnIconEl').click()  # click on call
        time.sleep(5)
        print("step----------------------1")





