import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
from configparser import ConfigParser
import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Ephangup:

    def __init__(self, url: str, driver):
        print("Constructor of End point hangup Handler")
        self.url = url
        self.driver = driver

    def doepcallhangup(self):
        print('checking2')
       
        try:
            self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            print('checking1')
            # to handle the unsecure site in browser
            time.sleep(3)
            self.driver.get(self.url)
            try:
                self.driver.find_element_by_xpath("//*[@id='details-button']").click()
                time.sleep(3)
                print('check')
                self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
            except NoSuchElementException as e:
                print('EP_hangup_file:',e)

            time.sleep(10)

            self.driver.find_element_by_xpath("//*[@id='splitbutton-1040-btnIconEl']").click()  # hangup the call
            print('Hanged up before')
            time.sleep(6)

        except Exception as e:
            print('Hanged up after')
            print('Result:', e)
            #self.driver.find_element_by_xpath("//*[@id='splitbutton-1040-btnIconEl']").click()  # hangup the call
            time.sleep(5)

