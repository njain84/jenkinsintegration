import time
import logging
from selenium import webdriver
import webbrowser
import openpyxl
from pywinauto.application import Application
import pyautogui
from configparser import ConfigParser
import unittest
import time


class Transfer_harman(unittest.TestCase):

    def test_report_transfer(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        self.driver.get('https://transfer.harman.com/')
        pyautogui.FAILSAFE = False
        time.sleep(5)
        self.driver.find_element_by_id('user_email').send_keys('njain')
        self.driver.find_element_by_id('user_password').send_keys('Symphony@123')
        self.driver.find_element_by_id('login-button-large').click()
        time.sleep(5)
        self.driver.find_element_by_id('message_recipients').send_keys('navneet.jain@harman.com,rajeev.Chauhan@harman.com,James.Quan@harman.com,Andrew.Qiu@harman.com,Daisy.Lin@Harman.com') #rajeev.Chauhan@harman.com,raj.Vardhan@harman.com
        self.driver.find_element_by_id('message_subject').send_keys('Smoke result ' + (parser.get('bug_tracker', 'build')))
        time.sleep(5)
        pyautogui.moveTo(550, 743)     #click on message body
        pyautogui.click()
        time.sleep(5)
        pyautogui.write('Hi All,')
        pyautogui.press('enter')  # press the Enter key
        pyautogui.write('Please find the attached smoke test report of Build ' + parser.get('bug_tracker', 'build'))
        pyautogui.press('enter')  # press the Enter key
        pyautogui.write('For a high level overview, please see Report_screen.png. For detailed report, download the allure-report.zip and open index.html.')
        time.sleep(5)
        self.driver.find_element_by_id('add_files_button').click()
        time.sleep(5)
        # will move to select the file
        pyautogui.moveTo(335, 65)
        pyautogui.click()
        time.sleep(10)
        pyautogui.press(['backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace',
                         'backspace', 'backspace', 'backspace', 'backspace', 'backspace'])
        time.sleep(5)
        pyautogui.write('C:/Jenkins/workspace/for_report_transfer')
        pyautogui.press('enter')  # press the Enter key
        time.sleep(3)
        pyautogui.moveTo(448, 358)
        pyautogui.click()
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'a')
        print('check here')
        time.sleep(2)
        pyautogui.press('enter')  # press the Enter key
        #pyautogui.moveTo(489, 458)
        #time.sleep(3)
        #pyautogui.click()
        time.sleep(20)
        self.driver.find_element_by_id('submit_button').click()
        time.sleep(10)

        if __name__ == '__main__':
            unittest.main()


