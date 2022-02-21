import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.EPlogin_call import Eplogin
from Login_config.EPlogin_callhangup import Ephangup
from selenium.webdriver.support.ui import Select

def EPlogin():

    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')

    myepcall = Eplogin('http://10.97.58.171', driver)
    myepcall.doepLogin()
    time.sleep(10)
    print("after first call")
    myephangup = Ephangup('http://10.97.58.171', driver)
    myephangup.doepcallhangup()


EPlogin()