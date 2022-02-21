import unittest
import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
from datetime import datetime
from datetime import datetime as dt
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class event_tab_Schedule_Recording():

    def __init__(self, driver):
        self.driver = driver

    def test_event_Schedule_Recording(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')#,options=options

        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        Myuserportallogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)
        Myuserportallogin.doLogin()

        #click on Administrator
        time.sleep(5)
        self.driver.find_elements_by_class_name('avatar_active')[0].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[2].click()
        #click on Events
        time.sleep(2)
        self.driver.find_element_by_link_text('Events').click()
        #clcick on Schedule Recording
        time.sleep(2)
        self.driver.find_element_by_link_text('Schedule Recording').click()
        time.sleep(2)
        self.driver.find_element_by_name('title').send_keys('regression_auto_start')
        self.driver.find_element_by_name('address').send_keys(parser.get('bug_tracker','vmr'))
        # It will reduce the end time
        self.driver.find_elements_by_class_name('col-sm-2')[1].click()
        time.sleep(2)
        action = ActionChains(self.driver)
        action.key_down(Keys.ARROW_UP).key_down(Keys.ARROW_UP).key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(5)
        self.driver.find_element_by_link_text('Advanced Information').click()
        time.sleep(2)
    def test_Auto_start_recording(self):
        

        self.driver.find_element_by_id('_vcmId_autoStart').click()
        time.sleep(1)
        
    def test_End_Automatically_call(self):

       self.driver.find_element_by_id('_vcmId_autoEnd').click()
       time.sleep(1)
        

    def test_final_scheddule_recording_result(self):

        # it will save the event
        self.driver.find_element_by_link_text('Save').click()
        time.sleep(2)
        minutes = dt.now().minute
        print(minutes)
        i = 1
        while i < 17:
            print(i)
            minutes = dt.now().minute
            if minutes == 15 or minutes == 30 or minutes == 45 or minutes == 00:
                break
            time.sleep(60)
            i += 1
        time.sleep(3)
        self.driver.refresh()
        time.sleep(13)
        # It will capture the status of call
        call_status = self.driver.find_elements_by_class_name('icon-hangup')[0].text
        print('call_staus',call_status)
        time.sleep(10)
        return call_status

    def test_Stop_event(self):
    
        self.driver.find_elements_by_class_name('btn_red')[0].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[1].click()

   
    def Navigate_to_event(self):
        time.sleep(2)
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        Myuserportallogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)
        Myuserportallogin.doLogin()
        # click on Join
        time.sleep(20)
        print('Navigation not done')
        #self.driver.find_elements_by_class_name('ng-binding')[29].click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[1]/vcm-live-list/div/div[1]/div[1]/div[2]/span[1]').click()
        print('Navigation done')





