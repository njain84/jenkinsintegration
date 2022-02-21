import unittest
import webbrowser

import pyautogui
import requests
import tkinter as tk
import time
import logging

#import self as self
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from Login_config.LoginHandler import Loginms
from Login_config.LoginHandleradminportal import Loginmsadmin

from configparser import ConfigParser

class adminportal_user_tab():

    def __init__(self, driver):

        self.driver = driver

    def delete_user(self):

        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        pyautogui.FAILSAFE = False
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)

        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        myloginadmin.doLoginadmin()
        time.sleep(4)
        self.driver.find_element_by_id("a_1016").click()
        self.driver.find_element_by_id("a_1017").click()
        time.sleep(3)
        # it will delete already created user
        try:
            self.driver.find_element_by_id('mainForm:user_Input').send_keys('Scriptctreatedadminuser', Keys.ENTER)
            time.sleep(2)
            self.driver.find_element_by_name('mainForm:j_idt28').click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt11_body']/button[5]").click()
            time.sleep(1)
            self.driver.find_element_by_id('dialogFirstBt').click()
        except WebDriverException as e:
            print('no user found:', e)
        time.sleep(3)

    def delete_multiple_user_and_group(self):

        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        pyautogui.FAILSAFE = False
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), self.driver)

        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        myloginadmin.doLoginadmin()
        time.sleep(4)
        self.driver.find_element_by_id("a_1016").click()
        self.driver.find_element_by_id("a_1017").click()
        time.sleep(3)
        # it will delete already created user
        try:
            for i in range (0,2):
                self.driver.find_element_by_id('mainForm:user_Input').click()
                pyautogui.hotkey('ctrl', 'a')
                self.driver.find_element_by_id('mainForm:user_Input').send_keys('testuser' + str(i), Keys.ENTER)
                time.sleep(2)
                self.driver.find_element_by_name('mainForm:j_idt35:0:j_idt37').click()
                time.sleep(2)
                self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt11_body']/button[5]").click()
                time.sleep(1)
                self.driver.find_element_by_id('dialogFirstBt').click()
                time.sleep(2)

        except WebDriverException as e:
            print('no user found:', e)
        finally:
            try:
                time.sleep(3)
                self.driver.find_element_by_id("a_1018").click()
                time.sleep(2)
                self.driver.find_element_by_id('mainForm:group_Input').send_keys('4709', Keys.ENTER)
                # it will click on edit
                time.sleep(2)
                self.driver.find_element_by_name('mainForm:j_idt32:0:j_idt34').click()
                time.sleep(2)
                self.driver.find_elements_by_class_name('btn')[6].click()
                time.sleep(2)
                self.driver.find_element_by_id('dialogFirstBt').click()
            except WebDriverException as e:
                print('group  not found:', e)
        time.sleep(2)

    def Add_Auditor(self):


        self.driver.find_element_by_id("a_1016").click()
        self.driver.find_element_by_id("a_1017").click()
        time.sleep(3)
        # it will click on Add button
        self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt11_body']/button[2]").click()
        time.sleep(3)
        # It will fill the user form
        self.driver.find_element_by_xpath("//input[@id='modalForm:Add-userID']").send_keys('scriptadmin', Keys.TAB,
                                                                                           'Scriptctreatedadminuser',
                                                                                           Keys.TAB, '123', Keys.TAB,
                                                                                           '123', Keys.TAB, Keys.TAB,
                                                                                           'abcd@gmail.com')

        select = Select(self.driver.find_element_by_id("modalForm:Add-userRole"))
        select.select_by_visible_text('Auditor')

        # It will click OK
        self.driver.find_element_by_id("addUser-Blt").click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(1)
        self.driver.find_element_by_link_text('Log Out').click()
        time.sleep(2)
        self.driver.close()

    def add_admin_user(self):

        # it will click on Add button
        self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt11_body']/button[2]").click()
        time.sleep(3)
        # It will fill the user form
        self.driver.find_element_by_xpath("//input[@id='modalForm:Add-userID']").send_keys('scriptadmin', Keys.TAB,
                                                                                           'Scriptctreatedadminuser',
                                                                                           Keys.TAB, '123', Keys.TAB,
                                                                                           '123', Keys.TAB, Keys.TAB,
                                                                                           'abcd@gmail.com')
        # it will click OK
        self.driver.find_element_by_id("addUser-Blt").click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(1)
        self.driver.find_element_by_link_text('Log Out').click()
        time.sleep(2)
        self.driver.close()
    def add_user(self):

        # it will click on Add button
        self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt11_body']/button[2]").click()
        time.sleep(3)
        # It will fill the user form
        self.driver.find_element_by_xpath("//input[@id='modalForm:Add-userID']").send_keys('scriptadmin', Keys.TAB,
                                                                                           'Scriptctreatedadminuser',
                                                                                           Keys.TAB, '123', Keys.TAB,
                                                                                           '123', Keys.TAB, Keys.TAB,
                                                                                           'abcd@gmail.com')
        select = Select(self.driver.find_element_by_id("modalForm:Add-userRole"))
        select.select_by_visible_text('User')

        # it will click OK
        self.driver.find_element_by_id("addUser-Blt").click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(1)
        self.driver.find_element_by_link_text('Log Out').click()
        time.sleep(2)
        self.driver.close()
    def add_multiple_users(self):

        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        #self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        #myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        #myloginadmin.doLoginadmin()
        time.sleep(2)
        self.driver.find_element_by_id("a_1016").click()
        self.driver.find_element_by_id("a_1017").click()
        time.sleep(2)
        for i in range(0, 2):
            # it will click on Add button
            self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt11_body']/button[2]").click()
            time.sleep(3)
            # It will fill the user form
            self.driver.find_element_by_xpath("//input[@id='modalForm:Add-userID']").send_keys('test' + str(i),
                                                                                               Keys.TAB,
                                                                                               'testuser' + str(i),
                                                                                               Keys.TAB, '123',
                                                                                               Keys.TAB,
                                                                                               '123', Keys.TAB,
                                                                                               Keys.TAB,
                                                                                               'abcd@gmail.com')

            select = Select(self.driver.find_element_by_id("modalForm:Add-userRole"))
            select.select_by_visible_text('User')

            # it will click OK
            self.driver.find_element_by_id("addUser-Blt").click()
            time.sleep(2)


    def Group(self):

        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        #self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        #myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        #myloginadmin.doLoginadmin()
        time.sleep(10)
        self.driver.find_elements_by_class_name('accordion-toggle')[5].click()
        #self.driver.find_element_by_id("a_1016").click()
        time.sleep(3)
        self.driver.find_element_by_id("a_1018").click()
        # click on add to add the group name
        time.sleep(3)
        self.driver.find_elements_by_class_name('btn')[4].click()
        # Enter the group name
        time.sleep(3)
        self.driver.find_element_by_id('modalForm:Add-groupName').send_keys('4709')
        time.sleep(2)
        self.driver.find_element_by_id('addGroup-Blt').click()
        # click the Group member
        time.sleep(2)
        #self.driver.find_element_by_link_text('Group Members').click()
        # it will search created group
        self.driver.find_element_by_id('mainForm:group_Input').send_keys('4709', Keys.ENTER)
        # it will click on edit
        time.sleep(2)
        self.driver.find_element_by_name('mainForm:j_idt32:0:j_idt34').click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[5].click()
        # it will click on group member
        time.sleep(2)
        self.driver.find_element_by_link_text('Group Members').click()
        time.sleep(2)
        # it will search the user which need to be added
        self.driver.find_element_by_id('modalForm:usersForEditGroup_Input').send_keys('test', Keys.ENTER)
        time.sleep(2)
        for i in range(0,2):

            self.driver.find_element_by_name('modalForm:j_idt28:'+str(i)+':j_idt30').click()

            time.sleep(2)
            # click on add button
            self.driver.find_elements_by_class_name('btn')[11].click()

            time.sleep(2)
        self.driver.find_element_by_id('editGroup-ok-blt').click()
        # Again go to search group and get count of users
        time.sleep(2)
        result=self.driver.find_element_by_xpath("//*[@id='group-table-row-0']/td[4]").text
        print(result)
        return result












