from pywinauto.application import Application
import time
from selenium.webdriver.support.ui import Select
import webbrowser
import os
import win32api
import pyautogui

def startrecording_rmxmanager():

        app = Application().start("C:/Program Files (x86)/Polycom/RmxManager V8.8.0/EMA/EMA.Coordinator/bin/Release_Web/RMX.Manager.exe")
        #app.start("C:/Program Files (x86)/Polycom/RmxManager V8.8.0/EMA/EMA.Coordinator/bin/Release_Web/RMX.Manager.exe")
        win = app.window(title='RMX Manager 8.8.0', top_level_only=True)
        #win = app.Dialog
        #win['Help'].click()
        #win.click_input("China-MS")
        #win.click_input("right")
        #win.right_click(pressed=''China-MS')
        time.sleep(12)
        #win.pyautogui.click(x=67, y=178)
        pyautogui.moveTo(70,202)
        pyautogui.doubleClick()         #Connecting the MCU
		time.sleep(3)
		self.pyautogui.press('enter')
        time.sleep(10)
        pyautogui.moveTo(177,515)       # Selecting the Conference
        time.sleep(5)
        pyautogui.click()
        time.sleep(6)
        pyautogui.moveTo(120, 460)       # Start the recording
        pyautogui.click()


        print('please click')
        #win.child_window(best_match='View').click()
        #win.print_control_identifiers()
        #win['Help'].select()
        # app.RMXManager880.MenuBar.MenuBarClickInput('#3->#0', app)  # View->Toolbars->Customize
        # app.controls.uia_controls.ButtonWrapper()
        #dlg = "RMX Manager 8.8.0"
        #app['RMX Manager 8.8.0'].menu_select("Help->About Polycom RMX")


startrecording_rmxmanager()




