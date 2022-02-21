import webbrowser
import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from Login_config.LoginHandleradminportal import Loginmsadmin
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io

class My_Meida_Center():

    #driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
    def __init__(self, driver):
        self.driver = driver


    def Click_My_Media_Center(self):
        #click on circle to open Media center
        self.driver.find_elements_by_class_name('avatar_active')[0].click()
        # click on My media center
        time.sleep(2)
        self.driver.find_elements_by_class_name('ng-binding')[7].click()

# Below function will search for the the VoD and select the closed caption
    def VoD_closed_caption(self):
        # it will search the video
        self.driver.find_element_by_xpath("//input[@ng-model='searchKey']").send_keys('10.216.17.172_202102260633502950',Keys.ENTER)
        time.sleep(1)
        self.driver.find_elements_by_class_name("link_edit_media")[0].click()
        # it will click on Manage close captions
        time.sleep(2)
        self.driver.find_element_by_link_text("Manage Closed Captions").click()
        #it will click on Automatic Generation captions
        time.sleep(1)
        self.driver.find_element_by_link_text("Automatic Generation").click()
        # it will select priority as critical
        select = Select(self.driver.find_element_by_xpath("//select[@ng-model='cielo24.result.priority']"))
        select.select_by_visible_text('Critical (less than 24 hours)')
        time.sleep(1)
        self.driver.find_element_by_id('enableTranslate').click()
        # It will click on generate
        time.sleep(5)
        self.driver.find_element_by_xpath("//p[@ng-click='translate2Text()']").click()
        time.sleep(1)
        progress = self.driver.find_elements_by_class_name("caption_list_column_language")[0].text
        print('Progress is:',progress)
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/button').click()
        return progress
    
    def click_edit(self):

        # It will click on edit
        self.driver.find_elements_by_class_name("link_edit_media")[0].click()
    def click_edit_properties(self):

        self.driver.find_element_by_link_text('Edit Properties').click()
    def click_enable_rating(self):

        self.driver.find_element_by_id('isRateEnableCheckBox').click()
        # It will click on OK
        self.driver.find_elements_by_class_name('btn')[81].click()
        
    def play_Vod(self):

        self.driver.find_element_by_xpath("//*[@id='MyMedias']/div[4]/div[3]/vcm-archive-list/div/div[5]/div/div/div[1]/a/div[2]").click()    



class Admin():

    def __init__(self, driver):
        self.driver = driver

    def third_party_integration(self):
        #click on Admin tab
        self.driver.find_element_by_link_text('Admin').click()
        #click on 3rd party integration option
        time.sleep(1)
        self.driver.find_element_by_link_text('3rd Party Integration').click()
        # select the Yes option in Enable speech to text
        time.sleep(2)
        self.select = Select(self.driver.find_element_by_xpath('//*[@id="Admin"]/div[2]/div/div/div/div/form/div[1]/div/select'))
        self.select.select_by_visible_text('Yes')
        # it will click on settings
        time.sleep(1)
        self.driver.find_elements_by_class_name('link_add_more')[0].click()
        time.sleep(1)
        #self.driver.find_elements_by_class_name('col-sm-5')[3].send_keys(Keys.TAB,'harma',Keys.TAB,'H@r-m@n1')
        self.driver.find_elements_by_class_name('col-sm-5')[3].click()
        # it will will the credentials of cielo24
        action = webdriver.ActionChains(self.driver)
        source = self.driver.find_elements_by_class_name('col-sm-5')[3]
        action.move_to_element(source).send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys('A').send_keys(Keys.DELETE).key_up(Keys.CONTROL).send_keys('harman').send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys('A').send_keys(Keys.DELETE).key_up(Keys.CONTROL).send_keys('H@r-m@n1').perform()
        #it will click on account test
        self.driver.find_elements_by_class_name('btn')[5].click()
        time.sleep(25)
        cielo_test_result = self.driver.find_elements_by_class_name('modal-body')[0].text
        print('result',cielo_test_result)
        time.sleep(2)
        #it will click on Ok(pop up)
        self.driver.find_elements_by_class_name('btn')[0].click()
        time.sleep(2)
        #it will click on save
        self.driver.find_elements_by_class_name('btn')[7].click()
        time.sleep(4)
        # it will save the Enable speech to text
        self.driver.find_elements_by_class_name('btn')[5].click()
        try:
            time.sleep(2)
            # it will click on popup
            self.driver.find_elements_by_class_name('btn')[0].click()
        except WebDriverException as e:
            print ( 'Already saved')




        return cielo_test_result
















