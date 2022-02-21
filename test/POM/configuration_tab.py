from configparser import ConfigParser

from selenium.common.exceptions import ElementNotInteractableException

from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium import webdriver
from pywinauto.application import Application
import time
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.common.keys import Keys


class config_server():


    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)




    def click_config(self):

        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        # login the admin portal
        myloginadmin.doLoginadmin()

        time.sleep(2)
        self.driver.find_elements_by_class_name('btn')[0].click()


    def click_System_time(self):
        self.driver.find_element_by_id('headerForm:j_idt10:3:j_idt12').click()
        # It will delete and fill the NTP server IP

    def Configure_NTP_server(self):

        #self.driver.find_element_by_id('headerForm:j_idt10:3:j_idt12').click()
        # It will delete and fill the NTP server IP
        time.sleep(1)
        self.driver.find_element_by_id('modalForm:ntpServer1_systemTime1').send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        self.driver.find_element_by_id('modalForm:ntpServer1_systemTime1').send_keys('10.99.236.150')
        time.sleep(1)
        self.driver.find_elements_by_class_name('btn')[9].click()
        # It will click ok on popup
        try:
            self.driver.implicitly_wait(3)

            self.driver.find_element_by_id('dialogFirstBt').click()
        except ElementNotInteractableException as e:
            print('Result for ok button',e)

    def NTP_server_current_time(self):

        self.driver.implicitly_wait(2)
        MS_time = self.driver.find_element_by_id('modalForm:sysTimepicker_systemTime1').get_attribute("value")
        #val = MS_time.get_attribute("value")
        print('time is',MS_time)
        return(MS_time)












