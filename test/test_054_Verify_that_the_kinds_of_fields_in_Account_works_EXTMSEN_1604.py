import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from Login_config.LoginHandleradminportal import Loginmsadmin
import unittest
from configparser import ConfigParser
from Login_config.LoginHandler import Loginms

from .POM.POM_admin_user_tab import adminportal_user_tab

class Accounts_verification(unittest.TestCase):


    def test_Accounts_verification(self):

        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        try:

            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)

            mylogin = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), driver)

            myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), driver)

            deleteuserandcreateadmin = adminportal_user_tab(driver)
            deleteuserandcreateadmin.delete_user()
            time.sleep(2)
            deleteuserandcreateadmin.add_admin_user()
            # login the admin portal
            driver.get(parser.get('bug_tracker', 'url'))
            time.sleep(3)
            driver.find_element_by_id('loginForm:userName').send_keys('scriptadmin')
            print("Hi")
            time.sleep(2)
            driver.find_element_by_id('loginForm:password').send_keys('123')
            time.sleep(3)
            driver.find_element_by_id('loginBtton').click()
            time.sleep(3)
            # confirm password
            driver.find_element_by_id('modalForm:PWD-oldPwd').send_keys('123')
            driver.find_element_by_id('modalForm:PWD-newPwd').send_keys('123')
            driver.find_element_by_id('modalForm:PWD-confirmPwd').send_keys('123')
            time.sleep(3)
            driver.find_element_by_id('setPwd-blt').click()

            driver.find_element_by_id('a_1000').is_displayed()
            time.sleep(3)
            # It will check the role of user and for Admin it should be administrator
            user_role = driver.find_elements_by_class_name('btn')[1].text
            print('User is', user_role)
            time.sleep(1)
            # It will click on on configuration tab
            driver.find_elements_by_class_name('btn')[0].click()
            driver.implicitly_wait(2)
            #It will check call setting option is available or not
            call_setting_option = driver.find_element_by_id('headerForm:j_idt10:0:j_idt12').text
            print('Option is available',call_setting_option)
            Template_option = driver.find_element_by_id('a_1006').text
            print('Template_option is', Template_option)
            # login user portal
            driver.get(parser.get('bug_tracker', 'urluserportal'))
            driver.find_element_by_id('login_user').send_keys('scriptadmin', Keys.TAB)
            print("Hi")

            driver.find_elements_by_class_name('form-control')[1].send_keys('123')

            driver.find_elements_by_class_name('btn')[0].click()

            time.sleep(5)
            result = driver.find_elements_by_class_name('btn')[0].text
            print(result)
            actual_result = 'Start Recording'
            assert actual_result == result, 'Fail'
            assert Template_option == 'Template',' Test case is failed as template tab is not available'
            assert call_setting_option == 'Call Settings', ' Test case is failed as template tab is not available'
            # It will verify user having user permission
            deleteuserandcreateadmin = adminportal_user_tab(driver)
            deleteuserandcreateadmin.delete_user()
            time.sleep(1)
            deleteuserandcreateadmin.add_user()

            # login the admin portal
            driver.get(parser.get('bug_tracker', 'url'))
            time.sleep(5)
            driver.find_element_by_id('loginForm:userName').send_keys('scriptadmin')
            print("Hi")
            time.sleep(2)
            driver.find_element_by_id('loginForm:password').send_keys('123')
            time.sleep(3)
            driver.find_element_by_id('loginBtton').click()
            time.sleep(3)
            login_text = driver.find_element_by_id('infoDetail').text
            print(login_text)
            actual_login_text = 'You are not an authorized user.'
            assert actual_login_text == login_text, 'User can login admin portal,EXTMSEN_1602'
            # -----------------------------------------------------------
            # login user portal
            driver.get(parser.get('bug_tracker', 'urluserportal'))
            driver.find_element_by_id('login_user').send_keys('scriptadmin', Keys.TAB)
            print("Hi")
            driver.find_elements_by_class_name('form-control')[1].send_keys('123')

            driver.find_elements_by_class_name('btn')[0].click()
            time.sleep(5)
            driver.find_element_by_id('oldPwd').send_keys('123', Keys.TAB, '123', Keys.TAB, '123', Keys.TAB,
                                                               Keys.TAB, Keys.ENTER)
            time.sleep(2)
            result = driver.find_elements_by_class_name('btn')[0].text
            print('result is:',result)
            actual_result = 'Start Recording'
            # it will check admin authorities are available for this user or not
            try:
                time.sleep(1)
                print('Start new code')
                # It will click on Mymediacenter
                driver.find_elements_by_class_name('avatar_active')[0].click()
                time.sleep(2)
                # It will click on MyMedia center
                driver.find_elements_by_class_name('btn')[2].click()
                time.sleep(2)
                #It will check admin tab
                driver.find_element_by_xpath('//*[@id="myTab"]/li[8]/a/span[1]').click()
            except WebDriverException as e:
                admin_tab = 'Admin tab not available'
                print('error is',e)
            admin_tab_compare = 'Admin tab not available'
            assert actual_result == result, 'Fail'
            assert admin_tab == admin_tab_compare, 'user has Admin tab access'
            #------------------------------------------------------------
            # It will verify Auditor user
            # It will delete the use
            deleteuserandcreateadmin = adminportal_user_tab(driver)
            deleteuserandcreateadmin.delete_user()
            time.sleep(2)
            # It will add auditor user
            deleteuserandcreateadmin.Add_Auditor()
            # login the admin portal
            driver.get(parser.get('bug_tracker', 'url'))
            time.sleep(5)
            driver.find_element_by_id('loginForm:userName').send_keys('scriptadmin')
            print("Hi")
            time.sleep(2)
            driver.find_element_by_id('loginForm:password').send_keys('123')
            time.sleep(3)
            driver.find_element_by_id('loginBtton').click()
            time.sleep(3)
            # Confirm Password
            driver.find_element_by_id('modalForm:PWD-oldPwd').send_keys('123')
            driver.find_element_by_id('modalForm:PWD-newPwd').send_keys('123')
            driver.find_element_by_id('modalForm:PWD-confirmPwd').send_keys('123')
            time.sleep(3)
            driver.find_element_by_id('setPwd-blt').click()
            time.sleep(2)
            # It will check system logs tab
            adminlogin = driver.find_element_by_id('a_1005').is_displayed()
            print('login', adminlogin)
            driver.refresh()
            time.sleep(10)
            driver.refresh()
            time.sleep(10)
            driver.refresh()
            time.sleep(10)
            driver.refresh()
            time.sleep(2)
            # It will check the
            auditor_logs = driver.find_elements_by_class_name('todayLog_download-btn')[0].is_displayed()
            print('logs',auditor_logs)
            actual_adminlogin = True
            actual_auditorlogs = True
            assert adminlogin == actual_adminlogin,'System logs tab is not present'
            assert auditor_logs == actual_auditorlogs,'download logs tab is not present'
            # -----------------------------------------------------------
            # login user portal
            driver.get(parser.get('bug_tracker', 'urluserportal'))
            driver.find_element_by_id('login_user').send_keys('scriptadmin', Keys.TAB)
            print("Hi")

            driver.find_elements_by_class_name('form-control')[1].send_keys('123')

            driver.find_elements_by_class_name('btn')[0].click()
            time.sleep(3)

            # Verifying not authorization
            login_text = driver.find_elements_by_class_name('form-group')[5].text
            print('permission', login_text)
            actual_login_text = 'Not enough permission.'
            assert actual_login_text == login_text, 'Auditor can login user portal,EXTMSEN_1601'

            driver.close()
        finally:
            deleteuserandcreateadmin = adminportal_user_tab(driver)
            deleteuserandcreateadmin.delete_user()





