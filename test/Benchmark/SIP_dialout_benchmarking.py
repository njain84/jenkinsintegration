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

from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io


def call_setup_benchmark_dialout():
    print("Hello....")
    parser = ConfigParser()
    parser.read('config.ini')
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
    mylogin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), driver)
    mylogin.doLoginadmin()
    time.sleep(5)

    for i in range(0,60):
        dt_string = now.strftime("%m-%d-%Y %I:%M:%S%p" + ' (GMT+05:30)')
        print('Time:',dt_string)

        try:
            driver.find_element_by_id('a_1001').click()
            time.sleep(3)
            driver.find_elements_by_class_name('btn')[4].click()  # opening the Dail out to Record page
            time.sleep(5)
            # select = Select(driver.find_element_by_id('modalForm:j_idt8'))  # Selecting the drop down
            # time.sleep(2)
            # select.select_by_visible_text('H.323')  # Selecting the H323
            # time.sleep(2)
            driver.find_elements_by_name('modalForm:address_p1')[0].send_keys('hdxsip177')
            time.sleep(2)
            driver.find_element_by_xpath("//button[@id='confirmDialOut']").click()  # Dail the call
            time.sleep(20)
            driver.find_element_by_id('dialogFirstBt').click()  # click the Ok if calls fails
            print('call failed', i)
            status = 'call failed-',i
            statusnew = str(status)
            with open('callfail.txt', 'a') as f:
                f.write("\n")
                f.write(dt_string)
                f.write(statusnew)
                f.close()

        except WebDriverException as e:
            print('Result:',e)
            print('Result1:call is established',i)
            statuspass = 'call passed-', i
            fstatus = str(statuspass)
            with open('callpass.txt', 'a') as f:
                f.write("\n")
                f.write(dt_string)
                f.write(fstatus)
                f.close()
                driver.find_element_by_id('mainForm:call_Input').click()
                pyautogui.hotkey('ctrl', 'a')
                driver.find_element_by_id('mainForm:call_Input').send_keys('hdxsip177',Keys.ENTER)
                time.sleep(30)
                driver.find_elements_by_class_name('portalTooltip')[0].click()  # Hang up the call.
                time.sleep(4)
                driver.find_element_by_xpath("//*[@id='dialogFirstBt']").click()
        i = i+1
        time.sleep(2)
    driver.quit()



call_setup_benchmark_dialout()
