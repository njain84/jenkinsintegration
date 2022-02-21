import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver

class Ephangup:

    def __init__(self, url: str, driver):
        print("Constructor of End point hangup Handler")
        self.url = url
        self.driver = driver

    def doepcallhangup(self):
        print('checking')
        self.driver.get(self.url)
        time.sleep(25)
        self.driver.find_element_by_xpath("//*[@id='splitbutton-1040-btnIconEl']").click()     #  hangup the call
        time.sleep(5)