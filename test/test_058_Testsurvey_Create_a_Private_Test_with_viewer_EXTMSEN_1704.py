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

class private_test(unittest.TestCase):


    def test_private_test_EXTMSEN_1704(self):

        try:
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
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
            test_survey_click.click_add_test()
            time.sleep(1)
            test_survey_click.create_private_test()
            time.sleep(1)
            test_survey_click.add_questions_in_test()
            time.sleep(2)
            test_survey_click.click_add_invitee()
            test_survey_click.add_single_invitee()
            time.sleep(2)
            test_survey_click.start_survey()
            time.sleep(2)
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            # It will login the user portal to check the created test
            myloginuser = Loginms('test1', 123, parser.get('bug_tracker', 'urluserportal'), driver)
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
            hex = Color.from_string(colour_test).hex
            test_survey_click = test_survey(driver)
            test_survey_click.click_survey_test()
            time.sleep(1)
            title = test_survey_click.take_survey()
            print('Returned title is:', title)
            time.sleep(1)
            # it will submit the answer
            test_survey_click.select_option_in_test()
            time.sleep(1)
            test_survey_click.click_submit_and_one_answer_in_test()
            time.sleep(3)
            certificate = test_survey_click.Check_the_certificate()
            print(certificate[0], certificate[1])
            time.sleep(2)
            # survey should not be visible to test2 user
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            myloginuser2 = Loginms('test2', 123, parser.get('bug_tracker', 'urluserportal'), driver)
            # login the user portal
            myloginuser2.doLogin()
            time.sleep(3)
            click_mediacenter = My_Meida_Center(driver)
            click_mediacenter.Click_My_Media_Center()
            time.sleep(2)
            test_survey_click = test_survey(driver)
            test_survey_click.click_survey_test()

            # It will check whether surevy is visible to test2 user or not
            try:
                time.sleep(2)
                # it will check title heading is present or not
                Check_title = driver.find_element_by_xpath(
                    '//*[@id="MySurveyList"]/div/div/div[3]/div[2]/div/div[1]/b').text
                print('Check_title is:', Check_title)
            except:
                Check_title = 'no_test'
                print('out of try block')
            time.sleep(1)
            # Now admin will login to get the number of responses
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            myloginuser2 = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), driver)
            # login the user portal
            myloginuser2.doLogin()
            time.sleep(3)
            click_mediacenter = My_Meida_Center(driver)
            click_mediacenter.Click_My_Media_Center()
            time.sleep(2)
            test_survey_click = test_survey(driver)
            test_survey_click.click_survey_test()
            time.sleep(1)
            Response = test_survey_click.collect_response()
            print('Response is:', Response)
            time.sleep(1)

        finally:

            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            myloginuser = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), driver)
            myloginuser.doLogin()
            time.sleep(3)
            click_mediacenter = My_Meida_Center(driver)
            click_mediacenter.Click_My_Media_Center()
            time.sleep(2)
            test_survey_click = test_survey(driver)
            test_survey_click.click_survey_test()
            time.sleep(2)
            test_survey_click.delete_survey()
            driver.close()

        assert title == 'Private_test', 'Survey is not created.'
        assert Response == '1', 'Response is not 1'
        assert Check_title == 'no_test', 'There is survey existing'
        assert certificate[0] == 'Certificate', 'Certificate has not been generated.'
        assert certificate[1] == 'Test1', 'user is wrong.'

