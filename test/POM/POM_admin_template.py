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
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class admin_Template():

    def __init__(self, driver):
        self.driver = driver

    def Recording_Template(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options) # ,options=options
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        # login the admin portal
        myloginadmin.doLoginadmin()

        time.sleep(5)
        self.driver.find_element_by_id('a_1006').click()
        time.sleep(1)
        self.driver.find_element_by_id('a_1007').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='rTemplate-table-row-0']/td[1]/input").click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('btn')[5].click()
        time.sleep(1)
    def Call_rate(self):
        time.sleep(2)
        self.select = Select(self.driver.find_element_by_id('modalForm:selmaxRate'))
        self.select.select_by_value('4096')
        time.sleep(5)
        # it will click on OK
        self.driver.find_elements_by_class_name('btn')[11].click()
    def Audio_only(self):
        time.sleep(2)
        # click on audio only
        self.driver.find_element_by_name('modalForm:checkboxAudioOnly').click()
        print('clicked')
        # it will click on OK
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()
    def enable_Live(self):

        # This code is to click and edit template
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='rTemplate-table-row-0']/td[1]/input").click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('btn')[5].click()
        #----end-----
        #click on live
        time.sleep(1)
        self.driver.find_element_by_name('modalForm:checkboxLive').click()
        print('clicked')
        # it will click on OK
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()
        time.sleep(1)
        self.driver.find_element_by_id('dialogFirstBt').click()
    def navigate_to_template(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options) # ,options=options
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        # login the admin portal
        myloginadmin.doLoginadmin()
        time.sleep(5)
        self.driver.find_element_by_id('a_1006').click()
        time.sleep(1)
        self.driver.find_element_by_id('a_1007').click()

    def add_new_template(self):
        # Add new recording template
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[4].click()
        time.sleep(2)
        self.driver.find_element_by_id('modalForm:templateName').send_keys('test')
        time.sleep(1)
        self.driver.find_element_by_id('modalForm:checkboxLive').click()
        time.sleep(2)
        self.driver.find_element_by_id('modalForm:checkboxLiveOnly').click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()

    def delete_template(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('mainForm:rTemplate_Input').send_keys('test')
        self.driver.implicitly_wait(5)
        self.driver.find_elements_by_class_name('btn')[2].click()
        time.sleep(2)
        self.driver.find_element_by_name("mainForm:j_idt28:0:j_idt30").click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[6].click()
        time.sleep(2)
        self.driver.find_element_by_id('dialogFirstBt').click()
        time.sleep(2)

    def create_vrr(self):
        # it will click vrr
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('a_1010').click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[4].click()
        time.sleep(2)
        # it will enter the name test
        self.driver.find_element_by_id('modalForm:vrrName').send_keys('test')
        time.sleep(2)
        # It will select the recording template test
        select=Select(self.driver.find_element_by_id('modalForm:vrrRecordingTemplate'))
        select.select_by_visible_text('test')
        #time.sleep(2)
        # it will select all transcoding template
        #self.driver.find_element_by_name('modalForm:vrr_outputTemplateaddAll').click()
        time.sleep(2)
        self.driver.find_element_by_id('confirmVRRAdd').click()
    def delete_vrr(self):
        # it will click on template
        time.sleep(2)
        #self.driver.find_element_by_id('a_1006').click()
        self.driver.implicitly_wait(2)
        # it will click vrr
        self.driver.find_element_by_id('a_1010').click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('mainForm:vrr_Input').send_keys('test')
        time.sleep(2)
        self.driver.find_elements_by_class_name('u_icon')[1].click()
        time.sleep(1)
        self.driver.find_element_by_name('mainForm:j_idt29:0:j_idt31').click()
        self.driver.find_elements_by_class_name('btn')[6].click()
        #It will click on OK
        time.sleep(2)
        self.driver.find_element_by_id('dialogFirstBt').click()

    def two_live_streaming(self):
        check = self.driver.find_element_by_id('modalForm:checkboxLive').is_selected()
        print('chck is',check)
        if check == False:
            # it will select live streaming
            self.driver.find_element_by_name('modalForm:checkboxLive').click()
        else:
            pass
        time.sleep(5)
        # it will click on live Live Streaming (MP4) Tab
        time.sleep(2)
        self.driver.find_element_by_link_text('Live Streaming (MP4)').click()
        time.sleep(2)
        #self.driver.find_element_by_id('modalForm:mp4RatePrimary').click()
        time.sleep(2)
        select = Select(self.driver.find_element_by_id('modalForm:mp4RatePrimary'))
        time.sleep(2)
        select.select_by_visible_text('384')
        time.sleep(1)
        # it will enter the name of the stream
        self.driver.find_element_by_id('modalForm:inputPrimaryAlias').send_keys(Keys.CONTROL,'a',Keys.DELETE,'Stream1')
        self.driver.find_element_by_id('modalForm:inputPrimaryAlias').send_keys('Stream1')
        time.sleep(10)
        #self.driver.find_element_by_id('modalForm:mp4RateSecond').click()
        time.sleep(2)
        select = Select(self.driver.find_element_by_id('modalForm:mp4RateSecond'))
        select.select_by_visible_text('320')
        time.sleep(1)
        self.driver.find_element_by_id('modalForm:inputSecondAlias').send_keys(Keys.CONTROL,'a',Keys.DELETE,)
        self.driver.find_element_by_id('modalForm:inputSecondAlias').send_keys('Stream2')
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()
        try:
            time.sleep(2)
            self.driver.find_element_by_id('dialogFirstBt').click()
            time.sleep(5)
            
        except ElementNotInteractableException as e:
            print(e)
            
    def wmv_streaming(self):

        #it will select the WMV
        self.driver.find_element_by_link_text('Live Streaming (WMV)').click()
        # It will select the streaming rate and name
        select = Select(self.driver.find_element_by_id('modalForm:wmvRatePrimary'))
        select.select_by_visible_text('384')
        time.sleep(1)
        self.driver.find_element_by_id('modalForm:inputPrimaryWMVAlias').send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        self.driver.find_element_by_id('modalForm:inputPrimaryWMVAlias').send_keys('wmv1')
        time.sleep(1)
        select = Select(self.driver.find_element_by_id('modalForm:wmvRateSecond'))
        select.select_by_visible_text('320')
        #self.driver.implicitly_wait(2)
        time.sleep(1)
        self.driver.find_element_by_id('modalForm:inputSecondWMVAlias').send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        self.driver.find_element_by_id('modalForm:inputSecondWMVAlias').send_keys('wmv2')
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()
        time.sleep(2)
    def disable_WMV_stream(self):
        # it will select the WMV
        self.driver.find_element_by_link_text('Live Streaming (WMV)').click()
        time.sleep(2)
        # It will select the streaming rate and name
        select = Select(self.driver.find_element_by_id('modalForm:wmvRatePrimary'))
        select.select_by_visible_text('Off')
        time.sleep(1)
        select = Select(self.driver.find_element_by_id('modalForm:wmvRateSecond'))
        select.select_by_visible_text('Off')
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()

    def Archiving(self):
        # It will click on Archiving tab
        self.driver.find_element_by_link_text('Archiving').click()

    def disable_one_live_stream(self):
        
     # it will click on live Live Streaming (MP4) Tab
        time.sleep(2)
        self.driver.find_element_by_link_text('Live Streaming (MP4)').click()
        time.sleep(2)
        # it will enter the name of the stream
        self.driver.find_element_by_id('modalForm:inputPrimaryAlias').send_keys(Keys.CONTROL,'a',Keys.DELETE)
        time.sleep(2)
        select = Select(self.driver.find_element_by_id('modalForm:mp4RateSecond'))
        select.select_by_visible_text('Off')
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()

    def Archiving(self):
        # It will click on Archiving tab
        self.driver.find_element_by_link_text('Archiving').click()

    def start_recording_immidiately(self):
        # It will check the status(enable/disable) the start_recording_immidiately option
        auto_recording_status = self.driver.find_element_by_id('modalForm:autoRecording').is_selected()
        print('auto_recording_status is :',auto_recording_status)
        if auto_recording_status == True:
            # It will click on the start_recording_immidiately option
            self.driver.find_element_by_id('modalForm:autoRecording').click()
        elif auto_recording_status == False:
            # It will click on the start_recording_immidiately option
            self.driver.find_element_by_id('modalForm:autoRecording').click()
        self.driver.find_elements_by_class_name('btn')[11].click()
        
    def Archive_Name_Prefix(self):

        #It will fill the Archive_Name_Prefix. First it will delete old data and will fill new name
        element = self.driver.find_element_by_id('modalForm:archivePrefix')
        element.send_keys(Keys.CONTROL, 'a',Keys.DELETE)
        #element.send_keys(Keys.DELETE)
        self.driver.find_element_by_id('modalForm:archivePrefix').send_keys('Autotest')
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[11].click()

    def click_on_Live_streaming_MP4(self):
        # It will check whether Live_stream_mp4 is enabled or not
        check = self.driver.find_element_by_id('modalForm:checkboxLive').is_selected()
        print('chck is', check)
        if check == False:
            # it will select live streaming
            self.driver.find_element_by_name('modalForm:checkboxLive').click()
        else:
            pass
        time.sleep(5)
        # it will  click on live Live Streaming (MP4) Tab
        time.sleep(2)
        self.driver.find_element_by_link_text('Live Streaming (MP4)').click()    

    def enable_H264_High_profile(self):

# It will enable the H.264 High profile
        time.sleep(1)
        check = self.driver.find_element_by_id('modalForm:enableLiveStreamingHP').is_selected()
        if check == False:

            self.driver.find_element_by_id('modalForm:enableLiveStreamingHP').click()
            self.driver.find_elements_by_class_name('btn')[11].click()




