from pywinauto.application import Application
import time
from selenium.webdriver.support.ui import Select
import webbrowser
import os
import win32api
import pyautogui

class RMXmanagerwithstoptrecording:

    def __init__(self,pyautogui):
        print("Rmxmanager H323 login")
        self.pyautogui = pyautogui

    def stoprecording(self):
        app = Application().start(
            "C:/Program Files (x86)/Polycom/RmxManager V8.8.0/EMA/EMA.Coordinator/bin/Release_Web/RMX.Manager.exe")
        # app.start("C:/Program Files (x86)/Polycom/RmxManager V8.8.0/EMA/EMA.Coordinator/bin/Release_Web/RMX.Manager.exe")
        win = app.window(title='RMX Manager 8.8.0', top_level_only=True)
        # win = app.Dialog
        # win['Help'].click()
        # win.click_input("China-MS")
        # win.click_input("right")
        # win.right_click(pressed=''China-MS')
        time.sleep(12)
        # win.pyautogui.click(x=67, y=178)
        self.pyautogui.moveTo(70, 202)
        self.pyautogui.doubleClick()  # Connecting the MCU
        time.sleep(10)
        self.pyautogui.moveTo(177, 515)  # Selecting the Conference
        time.sleep(5)
        self.pyautogui.click()
        time.sleep(20)
        self.pyautogui.moveTo(160, 460)  # Stop the recording
        self.pyautogui.click()


