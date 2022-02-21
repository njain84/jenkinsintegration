from pywinauto.application import Application
import time
from selenium.webdriver.support.ui import Select
import webbrowser
import os
import win32api
import pyautogui
import openpyxl
from configparser import ConfigParser


class RMXmanagerwithH323startrecording:

    def __init__(self,pyautogui):
        print("Rmxmanager H323 login")
        self.pyautogui = pyautogui

    def RMXmanagerH323(self):

            parser = ConfigParser()
            parser.read('config.ini')
            app = Application().start( "C:/Program Files (x86)/Polycom/RmxManager V8.8.0/EMA/EMA.Coordinator/bin/Release_Web/RMX.Manager.exe")
            # app.start("C:/Program Files (x86)/Polycom/RmxManager V8.8.0/EMA/EMA.Coordinator/bin/Release_Web/RMX.Manager.exe")
            win = app.window(title='RMX Manager 8.8.0', top_level_only=True)
            time.sleep(10)
            self.pyautogui.moveTo(70, 202)
            self.pyautogui.doubleClick()  # Connecting the MCU
            time.sleep(15)
            #self.pyautogui.moveTo(354, 990)   # going to drop down
            #time.sleep(3)
            #self.pyautogui.doubleClick()
            #time.sleep(2)
            #self.pyautogui.doubleClick()
            #time.sleep(2)
            self.pyautogui.moveTo(270, 950)      # clicking on Recording link
            self.pyautogui.click()
            time.sleep(15)
            self.pyautogui.moveTo(775, 270)      # click on specified recording link
            self.pyautogui.doubleClick()
            time.sleep(4)
            self.pyautogui.moveTo(450, 340)       # Click on Type
            self.pyautogui.doubleClick()
            time.sleep(3)
            self.pyautogui.moveTo(510, 340)
            self.pyautogui.click()
            time.sleep(3)
            self.pyautogui.moveTo(510, 355)  # selecting H323
            self.pyautogui.click()
            time.sleep(3)
            self.pyautogui.moveTo(510, 375)
            self.pyautogui.click()
            # This is additional functionality to configure RMX IP and registered name
            time.sleep(3)
            self.pyautogui.moveTo(510, 404)
            self.pyautogui.click()
            time.sleep(3)
            self.pyautogui.press(['backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace',
                                  'backspace', 'backspace', 'backspace', 'backspace', 'backspace'])
            time.sleep(2)
            self.pyautogui.write(parser.get('bug_tracker', 'MSIP'))  # Entering the IP
            time.sleep(2)
            self.pyautogui.moveTo(490, 477)
            time.sleep(3)
            self.pyautogui.click()
            self.pyautogui.press(['backspace', 'backspace', 'backspace', 'backspace'])
            time.sleep(3)
            self.pyautogui.write(parser.get('bug_tracker', 'msh323address'))   # Entering the alias name
            # End of additional functionality
            time.sleep(2)
            self.pyautogui.moveTo(525, 585)    #finally selected H323(OK)
            self.pyautogui.click()
            time.sleep(5)
            self.pyautogui.moveTo(177, 515)  # Selecting the Conference
            self.pyautogui.click()
            time.sleep(5)
            self.pyautogui.moveTo(120, 460)  # Start the recording
            self.pyautogui.click()










