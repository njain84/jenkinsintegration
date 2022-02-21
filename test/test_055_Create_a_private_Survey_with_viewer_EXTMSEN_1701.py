import unittest
import webbrowser
from datetime import datetime

import requests
import tkinter as tk
import time
import logging
from selenium import webdriver
from Login_config.LoginHandler import Loginms
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
from .POM.POM_My_media_center import My_Meida_Center
from .POM.survey_and_test import test_survey
from Login_config.LoginHandleradminportal import Loginmsadmin
import pytest


class Private_survey(unittest.TestCase):


    def test_private_survey_with_viewer(self):

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
        test_survey_click.private_survey()
        time.sleep(1)
        test_survey_click.add_question()
        time.sleep(2)
        test_survey_click.click_add_invitee()
        test_survey_click.add_single_invitee()
        time.sleep(1)
        test_survey_click.start_survey()
        time.sleep(1)
        driver.close()
        # Now to verify whether only defined user can see the survey or not
        # Dont add head less in this driver as not capturing title
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        myloginuser1 = Loginms('test1', 123, parser.get('bug_tracker', 'urluserportal'), driver)
        # login the admin portal
        myloginuser1.doLogin()
        time.sleep(3)
        click_mediacenter = My_Meida_Center(driver)
        click_mediacenter.Click_My_Media_Center()
        time.sleep(2)
        test_survey_click = test_survey(driver)
        test_survey_click.click_survey_test()
        time.sleep(2)
        # it will click on take survey
        title = test_survey_click.take_survey()
        print('Returned title is:', title)
        time.sleep(1)
        # it will submit the answer
        test_survey_click.select_option()
        time.sleep(1)
        driver.close()
        # survey should not be visible to test2 user
        # Dont add head less in this driver as not capturing title
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
            Check_title = 'no_survey'
            print('out of try block')
        # Now admin will login to get the number of responses
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)
        myloginuser2 = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), driver)
        # login the user portal
        myloginuser2.doLogin()
        time.sleep(2)
        click_mediacenter = My_Meida_Center(driver)
        click_mediacenter.Click_My_Media_Center()
        time.sleep(2)
        test_survey_click = test_survey(driver)
        test_survey_click.click_survey_test()
        time.sleep(1)
        Response = test_survey_click.collect_response()
        print('Response is:', Response)
        time.sleep(1)
        test_survey_click.delete_survey()
        driver.close()

        assert title == 'script_private_survey', 'Survey is not created.'
        assert Response == '1', 'Response is not 1'
        assert Check_title == 'no_survey', 'There is survey existing'





