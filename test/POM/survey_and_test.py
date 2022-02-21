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

class test_survey():

    def __init__(self, driver):
        self.driver = driver

    def click_survey_test(self):
        self.driver.find_element_by_link_text('Survey & Test').click()
    def collect_response(self):

        time.sleep(2)
        response = self.driver.find_element_by_xpath("//*[@id='MySurveyList']/div/div/div[3]/div[2]/div/div[3]").text
        return response
    def click_add_Survey(self):
        self.driver.find_element_by_link_text('Add Survey').click()
    def private_survey(self):
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('script_private_survey')
        time.sleep(1)
        select = Select(self.driver.find_elements_by_class_name('form-control')[4])
        select.select_by_visible_text('Private')
    def add_question(self):
        # it should take btn[8] but it is taking 6 dont know why
        self.driver.find_elements_by_class_name('btn')[6].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('test-question',Keys.TAB,Keys.TAB,'Yes',Keys.TAB,Keys.TAB,'No')
        time.sleep(1)
        self.driver.find_element_by_link_text('Save and Collect Invitee').click()
    def click_add_invitee(self):

        self.driver.find_element_by_link_text('Add').click()

    def add_single_invitee(self):
        self.driver.find_element_by_name('addChannelMember').send_keys('test1')
        time.sleep(2)
        source = self.driver.find_element_by_name('addChannelMember')
        source.send_keys(Keys.ARROW_DOWN,Keys.ENTER)
        time.sleep(1)
        self.driver.find_elements_by_class_name('btn')[7].click()
        time.sleep(1)
        #It will click on save and exit
        self.driver.find_elements_by_class_name('btn')[5].click()
    def start_survey(self):
        self.driver.find_elements_by_class_name('btn')[10].click()
        self.driver.implicitly_wait(2)
        self.driver.find_elements_by_class_name('btn')[1].click()
    def take_survey(self):

        title = self.driver.find_element_by_xpath('//*[@id="MySurveyList"]/div/div/div[3]/div[2]/div/div[1]/b').text
        self.driver.find_elements_by_class_name('btn')[10].click()
        return title
    def select_option(self):

        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ng-include/div[1]/div/div[1]/label/input').click()
        # it will submit the answer
        self.driver.find_elements_by_class_name('btn')[2].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('btn')[0].click()
    def delete_survey(self):

        self.driver.find_element_by_xpath("//*[@id='MySurveyList']/div/div/div[3]/div[2]/div/div[5]/a[3]").click()
        self.driver.implicitly_wait(3)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('delete')[0].click()
        self.driver.implicitly_wait(3)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(2)
		
    def click_add_test(self):

        self.driver.find_element_by_link_text('Add Test').click()
    def create_public_test(self):
        self.driver.implicitly_wait(3)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('Public_test',Keys.TAB,Keys.TAB,Keys.ENTER,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER)
    def add_questions_in_test(self):

        # It will click on add question
        # it should be 8 instead of 6 but it is taking 6 only so mentioned 6 after class
        self.driver.find_elements_by_class_name('btn')[6].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('How is HCS',Keys.TAB,Keys.TAB,'Good',Keys.TAB,Keys.TAB,'Bad')
        self.driver.find_element_by_xpath('//*[@id="menuContent"]/div/ui-view/div/div/div[2]/ui-view/div/div[2]/div[1]/div[1]/ui-view/form/div[2]/span/input').click()

        # It will add 2nd question
        # it should be 9 instead of 7 but it is taking 7 only so mentioned 7 after class
        self.driver.find_elements_by_class_name('btn')[7].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('How is Mediasuite', Keys.TAB, Keys.TAB, 'Good',Keys.TAB, Keys.TAB, 'Bad')
        self.driver.find_element_by_xpath('//*[@id="menuContent"]/div/ui-view/div/div/div[2]/ui-view/div/div[2]/div[1]/div[1]/ui-view/form/div[2]/span/input').click()
        # It will add 3rd question
        # it should be 9 instead of 7 but it is taking 7 only so mentioned 7 after class
        self.driver.find_elements_by_class_name('btn')[7].click()
        time.sleep(2)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('How are the Functionalities', Keys.TAB, Keys.TAB,'Good', Keys.TAB, Keys.TAB, 'Bad')
        self.driver.find_element_by_xpath('//*[@id="menuContent"]/div/ui-view/div/div/div[2]/ui-view/div/div[2]/div[1]/div[1]/ui-view/form/div[2]/span/input').click()
        #it will click on save
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menuContent"]/div/ui-view/div/div/h2/div[2]/a').click()

    def dot_colour(self):

        #backgcolour = self.driver.find_elements_by_class_name('tip_active')[3].value_of_css_property('background-color')   # It will check the back ground colour

        backgcolour = self.driver.find_element_by_xpath('// *[ @ id = "myTab"] / li[4] / a / span[2]').value_of_css_property('background-color')
        return backgcolour

    def select_option_in_test(self):

        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ng-include/div[1]/div/div[1]/label/input').click()

        # it will click on  the next
        time.sleep(1)
        self.driver.find_elements_by_class_name('btn')[1].click()
        # it will select another answer
        time.sleep(1)
        #self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ng-include/div[1]/div/div[1]/label/input').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ng-include/div[1]/div/div[2]/label/input').click()
        # it will click on  the next
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ng-include/div[2]/div[2]/button[2]').click()
        # it will select another answer
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ng-include/div[1]/div/div[1]/label/input').click()


    def click_submit_and_one_answer_in_test(self):

        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/ng-include/div[2]/div[2]/button[3]').click()
    def Check_the_certificate(self):

        certificate_generate = self.driver.find_element_by_xpath('//*[@id="defaultImage"]/div[1]/small').text

        user_name = self.driver.find_element_by_xpath('//*[@id="defaultImage"]/div[2]/b').text

        return certificate_generate,user_name
    def check_report(self):

        self.driver.find_element_by_xpath('//*[@id="MySurveyList"]/div/div/div[3]/div[2]/div/div[5]/a[1]').click()
        time.sleep(1)
        report = self.driver.find_element_by_xpath('//*[@id="menuContent"]/div/ui-view/div/div/div[2]/ui-view/div/h2/small[2]/a').text
        question = self.driver.find_element_by_xpath('//*[@id="menuContent"]/div/ui-view/div/div/div[2]/ui-view/div/div[1]/div/div/div[1]/div[1]').text
        return report,question
    def delete_test(self):

        self.driver.find_element_by_xpath('//*[@id="MySurveyList"]/div/div/div[3]/div[2]/div/div[5]/a[2]').click()
        self.driver.implicitly_wait(3)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('delete')[0].click()
        self.driver.implicitly_wait(3)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(2)
    def public_survey(self):
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('script_public_survey')
        time.sleep(1)
        select = Select(self.driver.find_elements_by_class_name('form-control')[4])
        select.select_by_visible_text('Public')
        
    def Everyone_see_result(self):
        self.driver.find_element_by_xpath('//*[@id="menuContent"]/div/ui-view/div/div/div[2]/ui-view/div/div[2]/div[1]/div[1]/ui-view/form/div[6]/div[1]/div/label/input').click()

    def create_private_test(self):
        self.driver.implicitly_wait(3)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys('Private_test', Keys.TAB, Keys.TAB,Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)        











