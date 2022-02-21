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
        print('checking')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath("//*[@id='details-button']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
            time.sleep(10)
            self.driver.find_element_by_xpath("//*[@id='splitbutton-1040-btnIconEl']").click()  # hangup the call
            print('Hanged up before')
        except Exception as e:
            print('Hanged up after')
            print('Result:', e)
            self.driver.find_element_by_xpath("//*[@id='splitbutton-1040-btnIconEl']").click()  # hangup the call
            time.sleep(5)
