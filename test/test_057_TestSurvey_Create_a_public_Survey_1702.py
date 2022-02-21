import unittest
import webbrowser
from datetime import datetime

import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from selenium.webdriver import ActionChains

from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
from .POM.POM_My_media_center import My_Meida_Center
from .POM.survey_and_test import test_survey
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium.webdriver.support.color import Color

class Everyone_see_survey(unittest.TestCase):

    def test_survey_test_all_see_survey(self):

        try:

            options = webdriver.ChromeOptions()

            options.add_argument('--headless')
            
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)
            
            # parser = ConfigParser()
            # parser.read('config.ini')
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            myloginuser = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), driver)
            # login the user portal
            myloginuser.doLogin()
            time.sleep(3)
            click_mediacenter = My_Meida_Center(driver)
            click_mediacenter.Click_My_Media_Center()
            time.sleep(2)
            test_survey_click = test_survey(driver)
            test_survey_click.click_survey_test()
            driver.implicitly_wait(5)
            test_survey_click.click_add_Survey()
            time.sleep(1)
            test_survey_click.public_survey()
            time.sleep(1)
            #test_survey_click.Everyone_see_result()
            test_survey_click. add_questions_in_test()
            time.sleep(2)
            test_survey_click.start_survey()
            time.sleep(2)
            result=[]
            hex = []
            for i in range(1,3):
                driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
                # It will login the user portal to check the created test
                myloginuser = Loginms('test'+str(i), 123, parser.get('bug_tracker', 'urluserportal'), driver)

                # login the user portal
                myloginuser.doLogin()
                time.sleep(3)
                click_mediacenter1 = My_Meida_Center(driver)
                click_mediacenter1.Click_My_Media_Center()
                time.sleep(2)

                time.sleep(2)
                colour_test = test_survey_click.dot_colour()
                print(Color.from_string((colour_test)))
                # It will convert from rgba to Hex
                hex.append(Color.from_string(colour_test).hex)
                test_survey_click = test_survey(driver)
                test_survey_click.click_survey_test()
                time.sleep(1)
                # it will click on take and will capture survey name
                title = test_survey_click.take_survey()
                print('Returned title is:', title)
                result.append(title)
                time.sleep(1)
                # it will submit the answer
                test_survey_click.select_option_in_test()
                time.sleep(1)
                test_survey_click.click_submit_and_one_answer_in_test()
                time.sleep(1)
                # it will click on Ok which reflects after submitting the answers
                driver.find_elements_by_class_name('btn')[0].click()
                time.sleep(5)
            print('Final list is',result)
            print(hex[0])


        finally:
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            myloginuser = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), driver)
            myloginuser.doLogin()
            time.sleep(3)
            click_mediacenter = My_Meida_Center(driver)
            click_mediacenter.Click_My_Media_Center()
            time.sleep(2)
            test_survey_click = test_survey(driver)
            test_survey_click.click_survey_test()
            time.sleep(2)
            test_survey_click.delete_test()
            time.sleep(2)


        assert result[0] == 'script_public_survey','Public survey is not completed for test1 user.'
        assert result[1] == 'script_public_survey','Public survey is not completed for test2 user.'
        # This assert might not be very useful as in all case we see red colour value #f62222 .
        assert hex[0] == '#f62222', 'Red dot is not exiting.'





