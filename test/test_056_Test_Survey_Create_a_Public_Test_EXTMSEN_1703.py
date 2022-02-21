import time
from selenium import webdriver
from Login_config.LoginHandler import Loginms
import unittest
from configparser import ConfigParser
from .POM.POM_My_media_center import My_Meida_Center
from .POM.survey_and_test import test_survey
from selenium.webdriver.support.color import Color

class Public_test(unittest.TestCase):


    def test_test_private_test_public(self):



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
            test_survey_click.click_add_test()
            time.sleep(1)
            test_survey_click.create_public_test()
            time.sleep(1)
            test_survey_click.add_questions_in_test()
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
            # It will login the MS user portal again and will check the report presence
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            # It will login the user portal to check the created test
            myloginuser = Loginms('admin', 123, parser.get('bug_tracker', 'urluserportal'), driver)
            myloginuser.doLogin()
            time.sleep(3)
            click_mediacenter2 = My_Meida_Center(driver)
            click_mediacenter2.Click_My_Media_Center()
            time.sleep(2)
            test_survey_click = test_survey(driver)
            test_survey_click.click_survey_test()
            time.sleep(1)
            report = test_survey_click.check_report()
            print(report[0], report[1])
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
            test_survey_click.delete_test()

        assert certificate[0] == 'Certificate','Certificate has not been generated.'
        #assert certificate[1] == 'Test1','user is wrong.'
        # This assert might not be very usefull as in all case we see red colour value #f62222 .
        assert hex == '#f62222','Red dot is not exiting.'
        assert report[0] == 'Download Report', 'Report is not generated'
        assert report[1] == '1. How is HCS','Report is not generated'













