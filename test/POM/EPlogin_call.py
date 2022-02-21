import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
import openpyxl
from configparser import ConfigParser

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
class Eplogin:

    def __init__(self, url: str, driver):
        print("Constructor of End point Login Handler")
        self.url = url
        self.driver = driver

    def doepLogin(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        time.sleep(20)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        time.sleep(10)
        self.driver.find_element_by_id('textfield-1061-inputEl').send_keys(
            parser.get('bug_tracker', 'vmr'))  # Entering the dialing number
        time.sleep(5)
        self.driver.find_element_by_id('button-1062-btnIconEl').click()  # click on call
        time.sleep(5)
        print("step----------------------1")
        # self.driver.find_element_by_id('splitbutton - 1040 - btnIconEl').click()     #  hangup the call



    def EPSIPcall(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        time.sleep(20)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        time.sleep(10)
        self.driver.find_element_by_id('textfield-1061-inputEl').send_keys(parser.get('bug_tracker', 'mssipaddress'))  # Entering the dialing number
        time.sleep(5)
        self.driver.find_element_by_id('button-1062-btnIconEl').click()  # click on call
        time.sleep(5)
        print("step----------------------1")

    def EPH323call(self):
        parser = ConfigParser()
        configFilePath = r'C:\Users\MediaSuite\PycharmProjects\PycharmProjects\Media_Suite Smoke\test\config.ini'
        parser.read('configFilePath')
        #parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        time.sleep(20)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        time.sleep(10)
        self.driver.find_element_by_id('textfield-1061-inputEl').send_keys(parser.get('bug_tracker', 'msh323address'))  # Entering the dialing number
        time.sleep(5)
        self.driver.find_element_by_id('button-1062-btnIconEl').click()  # click on call
        time.sleep(5)
        print("step----------------------1")

#The below code is to unregister the EP and call to MS from EP, Sip call
    def call_to_MSIP(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        try:
            self.driver.find_element_by_xpath("//*[@id='details-button']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        except WebDriverException as e:
            print('Result:', e)
                
        """
        #It will unregister the EP with GK
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@id='treeview-1049-record-ext-record-6']/td/div/span").click()
        time.sleep(5)
        self.driver.find_elements_by_class_name('x-tree-node-text')[7].click()
        time.sleep(5)
        self.driver.find_elements_by_class_name('x-tree-node-text')[9].click()
        time.sleep(4)
        # select the SIP
        self.driver.find_elements_by_class_name('x-panel-header-icon')[1].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('x-form-field')[20].click()
        time.sleep(2)
        a = ActionChains(self.driver)
        a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
        time.sleep(2)
        self.driver.find_elements_by_class_name('x-form-field')[21].click()
        time.sleep(2)
        a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
        time.sleep(2)
        # click on save button
        self.driver.find_elements_by_class_name('x-btn')[10].click()
        """
        time.sleep(3)
        self.driver.find_elements_by_class_name('x-tree-node-text')[0].click()  # click on place the call
        time.sleep(4)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        #self.driver.find_elements_by_class_name('x-header-text')[2].click()  # click the manual Dial
        time.sleep(10)
        self.driver.find_element_by_name('workField').send_keys(parser.get('bug_tracker', 'MSIP'))  # Entering the dialing number
        self.driver.implicitly_wait(3)  # it will select the SIP
        self.driver.find_elements_by_class_name('x-trigger-index-0')[4].click()
        time.sleep(2)
        action = webdriver.ActionChains(self.driver)
        source = self.driver.find_elements_by_class_name('x-boundlist-item')[1]
        action.move_to_element(source).click().perform()
        time.sleep(3) #click on call
        self.driver.find_elements_by_class_name('x-btn-icon-el')[9].click()
        now = datetime.now()
        dt_string = now.strftime("%m-%d-%Y %I:%M%p" + ' (GMT+05:30)')
        time.sleep(2)
        self.driver.quit()
        return dt_string

    def EP_SIP_registration(self):
        print('start EP SIP registration')
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        # It will register the EP with GK
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@id='treeview-1049-record-ext-record-6']/td/div/span").click()
        time.sleep(7)
        self.driver.find_elements_by_class_name('x-tree-node-text')[7].click()
        time.sleep(5)
        self.driver.find_elements_by_class_name('x-tree-node-text')[9].click()
        time.sleep(4)
        # select the SIP
        self.driver.find_elements_by_class_name('x-panel-header-icon')[1].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('x-form-field')[20].click()
        time.sleep(2)
        a = ActionChains(self.driver)
        a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.DELETE).key_up(Keys.DELETE).send_keys('10.97.52.22').perform()
        time.sleep(2)
        self.driver.find_elements_by_class_name('x-form-field')[21].click()
        time.sleep(2)
        a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.DELETE).key_up(Keys.DELETE).send_keys('10.97.52.22').perform()
        time.sleep(2)
        # click on save button
        self.driver.find_elements_by_class_name('x-btn')[10].click()
        time.sleep(3)
        print('EP is registered with DMA')
        self.driver.quit()
        
    def Only_unregister_EP(self):

        parser = ConfigParser()
        parser.read('config.ini')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        self.driver.get(self.url)
        
        # to handle the unsecure site in browser
        try:
            self.driver.find_element_by_xpath("//*[@id='details-button']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        except WebDriverException as e:
            print('Result:', e)
                
        #It will unregister the EP with GK
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@id='treeview-1049-record-ext-record-6']/td/div/span").click()
        time.sleep(5)
        self.driver.find_elements_by_class_name('x-tree-node-text')[7].click()
        time.sleep(5)
        self.driver.find_elements_by_class_name('x-tree-node-text')[9].click()
        time.sleep(4)
        # select the SIP
        self.driver.find_elements_by_class_name('x-panel-header-icon')[1].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('x-form-field')[20].click()
        time.sleep(2)
        a = ActionChains(self.driver)
        a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
        time.sleep(2)
        self.driver.find_elements_by_class_name('x-form-field')[21].click()
        time.sleep(2)
        a.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).key_down(Keys.DELETE).key_up(Keys.DELETE).perform()
        time.sleep(2)
        # click on save button
        self.driver.find_elements_by_class_name('x-btn')[10].click()
        time.sleep(2)
        self.driver.quit()
        
    def EP_to_MS_H323_IP_call(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver.get(self.url)
        # to handle the unsecure site in browser
        self.driver.find_element_by_xpath("//*[@id='details-button']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='proceed-link']").click()
        time.sleep(20)
        self.driver.find_element_by_id('ext-comp-1059_header_hd-textEl').click()  # click the manual Dial
        time.sleep(4)
        self.driver.find_element_by_id('textfield-1061-inputEl').send_keys(parser.get('bug_tracker', 'MSIP'))  # Entering the dialing number
        self.driver.implicitly_wait(3)  # it will select the H323
        self.driver.find_elements_by_class_name('x-trigger-index-0')[4].click()
        time.sleep(2)
        action = webdriver.ActionChains(self.driver)
        source = self.driver.find_elements_by_class_name('x-boundlist-item')[2]
        action.move_to_element(source).click().perform()
        time.sleep(5)
        self.driver.find_element_by_id('button-1062-btnIconEl').click()  # click on call
        now = datetime.now()
        dt_string = now.strftime("%m-%d-%Y %I:%M%p" + ' (GMT+05:30)')
        time.sleep(5)
        return dt_string 

        










