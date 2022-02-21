from selenium import webdriver
from configparser import ConfigParser

import time
from selenium.webdriver.common.keys import Keys

from Login_config.LoginHandleradminportal import Loginmsadmin


class update_default_password():

    def __init__(self):
        pass

    def test_update_default_password(self):
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        myloginadmin = Loginmsadmin('admin', 'Harman12#$', parser.get('bug_tracker', 'url'), driver)
        myloginadmin.doLoginadmin()
        driver.implicitly_wait(10)
        # it will get te test as Confirmation fom the Confirmation page
        #Actual_text = driver.find_element_by_id('dialogModalLabel').text
        #print(Actual_text)
        #Expected_text = 'Confirmation'
        #assert Actual_text == Expected_text, 'EXTMSEN-1652-Assert error:Confirmation page is not available'
        driver.find_element_by_id('dialogFirstBt').click()
        time.sleep(1)
        driver.find_element_by_id('modalForm:PWD-oldPwd').send_keys('Harman12#$',Keys.TAB,123,Keys.TAB,123)
        time.sleep(1)
        driver.find_element_by_id('setPwd-blt').click()
        time.sleep(1)
        driver.find_element_by_id('modalForm:storagePolicy_nfs3').click()
        time.sleep(2)
        initial_text = driver.find_element_by_id('modalForm:storagePolicy_nfs3').text
        print('Text is',initial_text)
        actual_text = initial_text.split('\n')
        Expected_text = ' Local Storage Only'
        
        assert actual_text[0] == Expected_text, 'EXTMSEN-1644-Assert error:password is not updated'



