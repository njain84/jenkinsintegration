import unittest
import webbrowser

import pyautogui
import requests
import tkinter as tk
import time
import logging


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Login_config.LoginHandler import Loginms
from Login_config.LoginHandleradminportal import Loginmsadmin

from configparser import ConfigParser
from selenium.webdriver.support.select import Select

from Login_config.LoginHandler import Loginms
from Login_config.LoginHandleradminportal import Loginmsadmin

from configparser import ConfigParser


class admin_Registration():

    def __init__(self, driver):
        self.driver = driver

        # it will register at UDP

    def admin_registration_udp_check(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options) #,options=options
        mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)

        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        myloginadmin.doLoginadmin()
        time.sleep(5)  # clicking on configuration tab
        self.driver.find_elements_by_class_name('btn')[0].click()
        time.sleep(2)  # selecting signalling setting
        self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
        time.sleep(2)  # selecting sip
        self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
        time.sleep(2)
        #it will capture the status of registration
        test1_var = self.driver.find_element_by_xpath("//*[@id='SIPRegStatus_signal1']").text
        print(test1_var)
        select = Select(self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1'))
        # it will choose UDP protocol
        select.select_by_visible_text('UDP')
        if test1_var == 'Offline' or None:
            # it will click OK
            self.driver.find_element_by_id('Sip-blt').click()    
            # it will click another ok button in case protocol is not UDP otherwise produce error and switch to except. This code in try will help if already UDP protocol is not set.
            try:
                time.sleep(3)
                self.driver.find_element_by_id('dialogFirstBt').click()
                time.sleep(15)
                self.driver.find_elements_by_class_name('btn')[10].click()
                # This code is to check the current protocol
                time.sleep(5)  # clicking on configuration tab
                self.driver.find_elements_by_class_name('btn')[0].click()
                time.sleep(2)  # selecting signalling setting
                self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
                time.sleep(2)  # selecting sip
                self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
                # it will capture the value of transport protocol
                protocol = self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1').get_attribute("value")
                print('transport protocol is in try:', protocol)
                return protocol

            except WebDriverException as e:
                print('exception error:', e)
                time.sleep(5)  # clicking on configuration tab
                self.driver.find_elements_by_class_name('btn')[0].click()
                time.sleep(2)  # selecting signalling setting
                self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
                time.sleep(2)  # selecting sip
                self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
                time.sleep(2)
                # it will capture the value of transport protocol
                protocol = self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1').get_attribute("value")
                print('transport protocol is in Except:', protocol)
                return protocol

        else:
            print('server is online so executing else part')
            time.sleep(2)
            self.driver.find_element_by_id(
                'modalForm:isRegSIPCheck_signal1').click()  # this click the Register to SIP Server
            time.sleep(3)  # will click and select the transport protocol
            select = Select(self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1'))
            select.select_by_visible_text('UDP')
            time.sleep(2)
            self.driver.find_element_by_id('Sip-blt').click()
            time.sleep(4)
            self.driver.find_element_by_id('dialogFirstBt').click()
            time.sleep(20)
            self.driver.find_elements_by_class_name('btn')[10].click()
            # This code is to check the current protocol
            print('clicked on 2nd Ok')
            time.sleep(5)  # clicking on configuration tab
            self.driver.find_elements_by_class_name('btn')[0].click()
            time.sleep(2)  # selecting signalling setting
            self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
            time.sleep(2)  # selecting sip
            self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
            protocol = self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1').get_attribute("value")
            print('transport protocol is:', protocol)
            self.driver.quit()
            return protocol

    def admin_registration_tcp_check(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')

        self.driver = webdriver.Chrome(
            'C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)#options=options
        # mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)

        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        myloginadmin.doLoginadmin()
        time.sleep(5)  # clicking on configuration tab
        self.driver.find_elements_by_class_name('btn')[0].click()
        time.sleep(2)  # selecting signalling setting
        self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
        time.sleep(2)  # selecting sip
        self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
        time.sleep(2)
        # it will capture the status of registration
        test1_var = self.driver.find_element_by_xpath("//*[@id='SIPRegStatus_signal1']").text
        print(test1_var)
        time.sleep(2)
        select = Select(self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1'))
        # it will choose TCP protocol
        select.select_by_visible_text('TCP')
        if test1_var == 'Offline' or None:
            # it will click OK
            self.driver.find_element_by_id('Sip-blt').click()
            # it will click another ok button in case protocol is not TCP otherwise produce error and switch to except. This code in try will help if already tcp protocol is not set.
            try:
                time.sleep(3)
                self.driver.find_element_by_id('dialogFirstBt').click()
                time.sleep(15)
                self.driver.find_elements_by_class_name('btn')[10].click()
                # This code is to check the current protocol
                time.sleep(5)  # clicking on configuration tab
                self.driver.find_elements_by_class_name('btn')[0].click()
                time.sleep(2)  # selecting signalling setting
                self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
                time.sleep(2)  # selecting sip
                self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
                # it will capture the value of transport protocol
                protocol = self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1').get_attribute("value")
                print('transport protocol is in try:', protocol)
                return protocol

            except WebDriverException as e:
                print('exception error:', e)
                time.sleep(5)  # clicking on configuration tab
                self.driver.find_elements_by_class_name('btn')[0].click()
                time.sleep(2)  # selecting signalling setting
                self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
                time.sleep(2)  # selecting sip
                self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
                time.sleep(2)
                # it will capture the value of transport protocol
                protocol = self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1').get_attribute("value")
                print('transport protocol is in Except:', protocol)
                return protocol

        else:
            print('server is online so executing else part')
            time.sleep(2)
            self.driver.find_element_by_id(
                'modalForm:isRegSIPCheck_signal1').click()  # this click the Register to SIP Server
            time.sleep(3)  # will click and select the transport protocol
            select = Select(self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1'))
            select.select_by_visible_text('TCP')
            time.sleep(2)
            self.driver.find_element_by_id('Sip-blt').click()
            time.sleep(4)
            self.driver.find_element_by_id('dialogFirstBt').click()
            time.sleep(20)
            self.driver.find_elements_by_class_name('btn')[10].click()
            # This code is to check the current protocol
            print('clicked on 2nd Ok')
            time.sleep(5)  # clicking on configuration tab
            self.driver.find_elements_by_class_name('btn')[0].click()
            time.sleep(2)  # selecting signalling setting
            self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
            time.sleep(2)  # selecting sip
            self.driver.find_element_by_xpath("//*[@id='signalTab_signal1']/li[2]/a").click()
            protocol = self.driver.find_element_by_id('modalForm:SIP-TransportType_signal1').get_attribute("value")
            print('transport protocol is:', protocol)
            self.driver.quit()
            return protocol

    def test_H323_unregister(self):

        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options) #,options=options
        mylogin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        mylogin.doLoginadmin()
        time.sleep(5)  # clicking on configuration tab
        self.driver.find_elements_by_class_name('btn')[0].click()
        time.sleep(2)  # selecting signalling setting
        self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
        time.sleep(4)
        checkbox_value = self.driver.find_element_by_xpath("//*[@id='modalForm:isRegToGKEnableCheck_signal1']").get_attribute('checked')
        print('Checkbox is:', checkbox_value)
        if checkbox_value == 'true':
            self.driver.find_element_by_xpath("//*[@id='modalForm:isRegToGKEnableCheck_signal1']").click()  # this click the Register to  Server
            # time.sleep(3)
            # self.driver.find_element_by_xpath("//*[@id='modalForm:primaryGKIP_signal1']").send_keys('10.97.58.167') # it will put the DMA IP
            # time.sleep(3)    # fill the System Prefix | E.164
            # self.driver.find_element_by_xpath("//*[@id='modalForm:sysPrefix_signal1']").send_keys(parser.get('bug_tracker', 'msh323address'))
            # time.sleep(3)  # fill the System H.323 Alias
            # self.driver.find_element_by_xpath("//*[@id='modalForm:sysH323Alias_signal1']").send_keys(parser.get('bug_tracker', 'msh323address'))

            time.sleep(4)
            self.driver.find_element_by_id('Sip-blt').click()  # click OK
            try:
                time.sleep(3)
                self.driver.find_element_by_id('dialogFirstBt').click()  # OK pop up
                time.sleep(40)
                self.driver.find_element_by_id('dialogFirstBt').click()  # OK another popup
            except WebDriverException as e:
                print('Result:', e)
            time.sleep(5)  # clicking on configuration tab
            self.driver.find_elements_by_class_name('btn')[0].click()
            time.sleep(2)  # selecting signalling setting
            self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
            time.sleep(7)  # Now it will see the status using below
            test1_var = self.driver.find_element_by_xpath("//*[@id='isEnablePrimaryGK_signal1']").text
            print(test1_var)
            time.sleep(5)
        else:
            #self.driver.find_element_by_xpath("//*[@id='modalForm:isRegToGKEnableCheck_signal1']").click()  # this click the Register to  Server
            # time.sleep(3)
            # self.driver.find_element_by_xpath("//*[@id='modalForm:primaryGKIP_signal1']").send_keys('10.97.58.167') # it will put the DMA IP
            # time.sleep(3)    # fill the System Prefix | E.164
            # self.driver.find_element_by_xpath("//*[@id='modalForm:sysPrefix_signal1']").send_keys(parser.get('bug_tracker', 'msh323address'))
            # time.sleep(3)  # fill the System H.323 Alias
            # self.driver.find_element_by_xpath("//*[@id='modalForm:sysH323Alias_signal1']").send_keys(parser.get('bug_tracker', 'msh323address'))

            time.sleep(4)
            self.driver.find_element_by_id('Sip-blt').click()  # click OK
            try:
                time.sleep(3)
                self.driver.find_element_by_id('dialogFirstBt').click()  # OK pop up
                time.sleep(44)
                self.driver.find_element_by_id('dialogFirstBt').click()  # OK another popup
            except WebDriverException as e:
                print('Result:', e)
            time.sleep(5)  # clicking on configuration tab
            self.driver.find_elements_by_class_name('btn')[0].click()
            time.sleep(2)  # selecting signalling setting
            self.driver.find_element_by_id('headerForm:j_idt10:1:j_idt12').click()
            time.sleep(7)  # Now it will see the status using below
            test1_var = self.driver.find_element_by_xpath("//*[@id='isEnablePrimaryGK_signal1']").text
            print(test1_var)
        return test1_var
        

















