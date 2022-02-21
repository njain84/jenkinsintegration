import time
from selenium import webdriver
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import io
import unittest
from configparser import ConfigParser
import openpyxl
from selenium.common.exceptions import TimeoutException, WebDriverException
import re
from .POM.EPlogin_callhangup import Ephangup
class AES(unittest.TestCase):

    def test_AES(self):
        try:
            print("Hello....")
            parser = ConfigParser()
            parser.read('config.ini')
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options) #options=options
            myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
            myloginadmin.doLoginadmin()
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[@id='a_1006']").click() #click on Template
            time.sleep(3)
            self.driver.find_element_by_xpath("// *[ @ id = 'a_1007']").click()  # click on Recording Templates
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='rTemplate-table-row-0']/td[1]/input").click() #Click on Default Recording
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt7_body']/button[3]").click() #click on edit
            time.sleep(3)
            self.select1 = Select(self.driver.find_element_by_xpath("//*[@id='modalForm:sel_aestype']")) # Media encryption type
            time.sleep(2)
            self.select1.select_by_visible_text('Required for All Calls')
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='modalForm:modalPanel_body']/div[3]/button[2]").click() #click ok
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='a_1001']").click() # click on call tab
            time.sleep(8)
            self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt8_body']/button[2]").click() # click on Dial out to record
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='modalForm:address_p1']").send_keys(parser.get('bug_tracker', 'rpdH323address')) # click on Address
            time.sleep(3)
            self.select1 = Select(self.driver.find_element_by_xpath("//*[@id='modalForm:j_idt8']"))
            self.select1.select_by_visible_text("H.323") # selecting H323
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='confirmDialOut']").click() #click OK
            time.sleep(25)
            self.driver.find_element_by_xpath("//*[@id='portalPopoverCall-0']").click()
            time.sleep(5)
            pertext = self.driver.find_elements_by_class_name('popover-content')[0].text
            print(pertext)
            # This code is to fetch the information from detail tab and convert it into list. at last it will split the list and fetch the call rate.
            x = [pertext]
            print('Total values :', pertext)
            encryption = x[0].split('\n')
            print('encryption :', encryption)
            encryption1 = encryption[8]
            encryption2 = encryption1.split('Encryption ', 1)
            match = encryption2[1]
            print('Final encryption is',match)
            time.sleep(2)
            self.driver.refresh()
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='a_1001']").click()  # click on call tab
            time.sleep(3)
            self.driver.find_elements_by_class_name('portalTooltip')[0].click()  # Hang up the call
            time.sleep(2)
            self.driver.find_element_by_xpath("// *[ @ id = 'dialogFirstBt']").click()
            time.sleep(5)
            # Change it to Encryption OFF and try H323 call
            time.sleep(2)
            self.driver.find_elements_by_class_name('btn')[0].click()  # click on configuration
            time.sleep(2)
            self.driver.find_element_by_id('headerForm:j_idt10:0:j_idt12').click()
            print('test')
            time.sleep(5)
            Encryption_call_setting = Select(self.driver.find_element_by_id("modalForm:sel_aestype")) # Media encryption type
            time.sleep(2)
            print('test2')
            Encryption_call_setting.select_by_value('3')
            print('test3')
            time.sleep(2)
            self.driver.find_elements_by_class_name('btn')[9].click()
            time.sleep(3)
            self.driver.find_element_by_id('dialogFirstBt').click()
            time.sleep(25)
            self.driver.find_element_by_id('dialogFirstBt').click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[@id='a_1006']").click()  # click on Template
            time.sleep(3)
            self.driver.find_element_by_xpath("// *[ @ id = 'a_1007']").click()  # click on Recording Templates
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='rTemplate-table-row-0']/td[1]/input").click()  # Click on Default Recording
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt7_body']/button[3]").click()  # click on edit
            time.sleep(3)
            self.select1 = Select(self.driver.find_element_by_xpath("//*[@id='modalForm:sel_aestype']"))  # Media encryption type
            time.sleep(2)
            self.select1.select_by_visible_text('Off')
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='modalForm:modalPanel_body']/div[3]/button[2]").click()  # click
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='a_1001']").click()  # click on call tab
            time.sleep(40) # Wait for recording service to come up
            self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt8_body']/button[2]").click()  # click on Dial out to record
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='modalForm:address_p1']").send_keys(parser.get('bug_tracker', 'rpdH323address'))  # click on Address
            time.sleep(3)
            self.select1 = Select(self.driver.find_element_by_xpath("//*[@id='modalForm:j_idt8']"))
            time.sleep(1)
            self.select1.select_by_visible_text("H.323")  # selecting H323
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='confirmDialOut']").click()  # click OK
            time.sleep(25)
            self.driver.find_element_by_xpath("//*[@id='portalPopoverCall-0']").click()
            time.sleep(5)
            pertext1 = self.driver.find_elements_by_class_name('popover-content')[0].text
            print(pertext1)
            # This code is to fetch the information from detail tab and convert it into list. at last it will split the list and fetch the call rate.
            y = [pertext1]
            print('Total values :', pertext1)
            dencryption = y[0].split('\n')
            print('dencryption :', dencryption)
            dencryption1 = dencryption[8]
            dencryption2 = dencryption1.split('Encryption ', 1)
            match1 = dencryption2[1]
            print('Final match1 encryption is', match1)
            #self.driver.find_element_by_xpath("//*[@id='portalPopoverCall-0']").click()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='a_1001']").click()  # click on call tab
            time.sleep(3)
            self.driver.find_elements_by_class_name('portalTooltip')[0].click()  # Hang up the call
            time.sleep(2)
            self.driver.find_element_by_xpath("// *[ @ id = 'dialogFirstBt']").click()
            time.sleep(10)
            #self.assertIsNotNone(match, "EXTMSEN-1637-Assert error: Test case is failed because Encryption is disabled")
            assert (match == 'AES_256' or match =='AES_128'),"EXTMSEN-1637-Assert error: Test case is failed because Encryption is disabled"
            assert match1 == 'OFF', "EXTMSEN-1637-Assert error: Test case is failed because Encryption is enabled"

        finally:
            try:
                print('finally')
                parser = ConfigParser()
                parser.read('config.ini')
                self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
                try:
                    time.sleep(2)
                    Epcallhangup = Ephangup(parser.get('bug_tracker', 'epurl'), self.driver)
                    Epcallhangup.doepcallhangup()
                except WebDriverException as e:
                    print('Ep is already disconnected:', e)

                myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
                myloginadmin.doLoginadmin()
                time.sleep(5)
                self.driver.find_elements_by_class_name('btn')[0].click()  # click on configuration
                time.sleep(2)
                self.driver.find_element_by_id('headerForm:j_idt10:0:j_idt12').click()
                print('test')
                time.sleep(5)
                Encryption_call_setting = Select(self.driver.find_element_by_id("modalForm:sel_aestype")) # Media encryption type
                time.sleep(2)
                Encryption_call_setting.select_by_value('2')
                time.sleep(2)
                self.driver.find_elements_by_class_name('btn')[11].click()
                time.sleep(2)
                self.driver.find_element_by_id('dialogFirstBt').click()
                time.sleep(25)
                self.driver.find_element_by_id('dialogFirstBt').click()
            
                self.driver.find_element_by_xpath("//*[@id='a_1006']").click()  # click on Template
                time.sleep(3)
                self.driver.find_element_by_xpath("// *[ @ id = 'a_1007']").click()  # click on Recording Templates
                time.sleep(3)
                self.driver.find_element_by_xpath("//*[@id='rTemplate-table-row-0']/td[1]/input").click()  # Click on Default Recording
                time.sleep(3)
                self.driver.find_element_by_xpath("//*[@id='mainForm:j_idt7_body']/button[3]").click()  # click on edit
                time.sleep(3)
                self.select1 = Select(self.driver.find_element_by_xpath("//*[@id='modalForm:sel_aestype']"))  # Media encryption type
                time.sleep(2)
                self.select1.select_by_visible_text('When Available')
                time.sleep(2)
                self.driver.find_element_by_xpath("//*[@id='modalForm:modalPanel_body']/div[3]/button[2]").click()  # click
                time.sleep(3)
                self.driver.find_element_by_xpath("//*[@id='a_1001']").click()  # click on call tab
                time.sleep(3)
                self.driver.find_element_by_xpath("//*[@id='call-table-row-0']/td[2]/a/img").click()  # Hang up the call
                time.sleep(5)
                self.driver.find_element_by_xpath("// *[ @ id = 'dialogFirstBt']").click()
                time.sleep(10)
                self.driver.close()


            except WebDriverException as e:
                print('Result:', e)



    if __name__ == '__main__':
        unittest.main()








