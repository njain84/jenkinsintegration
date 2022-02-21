from datetime import datetime
import webbrowser

import pyautogui
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from win32com.test.testPersist import now
from EPlogin_call import Eplogin
from EPlogin_callhangup import Ephangup
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io


def call_setup_benchmark_dialout():
    print("Hello....")
    parser = ConfigParser()
    parser.read('config.ini')
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')

    for i in range(0,60):

        dt_string = now.strftime("%m-%d-%Y %I:%M:%S%p" + ' (GMT+05:30)')
        print('Time:', dt_string)
        print('loopagain:', i)
        myepcall = Eplogin(parser.get('bug_tracker', 'epurl'), driver)  # Login the EP
        myepcall.EPSIPcall()
        time.sleep(2)
        try:
            mylogin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), driver)
            mylogin.doLoginadmin()
            time.sleep(10)
            driver.find_element_by_id('a_1001').click()
            time.sleep(3)
            # Search and hang up the required call
            driver.find_element_by_id('mainForm:call_Input').click()
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'a')
            driver.find_element_by_id('mainForm:call_Input').send_keys('GSS171', Keys.ENTER)
            time.sleep(30)
            driver.find_elements_by_class_name('portalTooltip')[0].click()  # Hang up the call.
            time.sleep(4)
            driver.find_element_by_xpath("//*[@id='dialogFirstBt']").click()
            print('call Pass', i)
            status = 'call Pass-', i
            statusnew = str(status)
            with open('callpassdialin.txt', 'a') as f:
                f.write("\n")
                f.write(dt_string)
                f.write(statusnew)
                f.close()

        except (WebDriverException,IndexError) as e:
            print('Result:',e)
            print('Result1:call is failed',i)
            statuspass = 'call fialed-', i
            fstatus = str(statuspass)
            with open('callfaildialin.txt', 'a') as f:
                f.write("\n")
                f.write(dt_string)
                f.write(fstatus)
                f.close()
            try:
                ephangup = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
                ephangup.doepcallhangup()
            except WebDriverException as e:
                print('Epcallhangup:',e)

        time.sleep(2)


        i = i+1
        time.sleep(5)
    driver.close()

call_setup_benchmark_dialout()
