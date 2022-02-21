import time
import logging
from selenium import webdriver
import pyautogui
from Login_config.LoginHandleradminportal import Loginmsadmin
from configparser import ConfigParser
import unittest
import openpyxl
import allure


class System_upgrade(unittest.TestCase):

    def test_System_upgrade(self):
        print("Hello....")
        parser = ConfigParser()
        parser.read('config.ini')
        hostname = parser.get('bug_tracker', 'MSIP')
        self.driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        mylogin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), self.driver)
        mylogin.doLoginadmin()
        time.sleep(15)
        # click on Admin tab
        self.driver.find_element_by_xpath("//*[@id='a_1019']").click()
        time.sleep(3)
        # click on Product activation
        self.driver.find_element_by_xpath("//*[@id='a_1020']").click()
        time.sleep(3)
        version = self.driver.find_element_by_xpath("//*[@id='normalLicenseDiv']/div[2]/label[2]").text
        print('Software Version is', version)
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[ @ id = 'a_1021']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("// *[ @ id = 'mainForm:isLicenseAgreeCheck']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("// *[ @ id = 'mainForm:checkboxValidateCert']").click()
        time.sleep(3)
        self.driver.find_element_by_id('btnUploadSelect').click()
        time.sleep(5)
        pyautogui.moveTo(275, 50)
        pyautogui.click()
        time.sleep(2)
        pyautogui.press(
            ['backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace', 'backspace',
             'backspace', 'backspace', 'backspace', 'backspace'])
        time.sleep(2)
        pyautogui.write("C:/release/latest")
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.moveTo(380, 155)
        pyautogui.doubleClick()
        time.sleep(200)
        # click upgrade button
        self.driver.find_element_by_xpath("// *[ @ id = 'upgradeOKButton']").click()
        time.sleep(3)
        self.driver.find_element_by_id('dialogFirstBt').click()
        time.sleep(200)
        #It will create an empty file named test
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=22, username='root', password='1J$yZqk{8kgMxbw')
        stdin, stdout, stderr = ssh.exec_command('touch test')
        stdin, stdout, stderr = ssh.exec_command('ls')
        print(f'STDOUT: {stdout.read().decode("utf8")}')
        stdout.close()
        stdin.close()
        stderr.close()
        ssh.close()
        #file creation is finished
        time.sleep(5)
        mylogin.doLoginadmin()
        time.sleep(5)
        # click on Admin tab
        self.driver.find_element_by_xpath("//*[@id='a_1019']").click()
        time.sleep(3)
        # click on Product activation
        self.driver.find_element_by_xpath("//*[@id='a_1020']").click()
        time.sleep(5)
        newversion = self.driver.find_element_by_xpath("//*[@id='normalLicenseDiv']/div[2]/label[2]").text
        # it will fill the new version in ini file
        a_file = open("c:/PycharmProjects/PycharmProjects/Media_Suite_Smoke/test/Newtest/config.ini", "r")

        list_of_lines = a_file.readlines()
        # list_of_lines[1] = "build = MediaSuite-\n"
        list_of_lines[11] = 'build = mediasuite-' + newversion
        a_file = open("c:/PycharmProjects/PycharmProjects/Media_Suite_Smoke/test/Newtest/config.ini", "w")
        a_file.writelines(list_of_lines)
        a_file.close()
        # It will fill the new version in ini file for report

        a_file = open("c:/PycharmProjects/PycharmProjects/Media_Suite_Smoke/test/Report_email/config.ini", "r")

        list_of_lines = a_file.readlines()
        # list_of_lines[1] = "build = MediaSuite-\n"
        list_of_lines[11] = 'build = mediasuite-' + newversion
        a_file = open("c:/PycharmProjects/PycharmProjects/Media_Suite_Smoke/test/Report_email/config.ini", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

        assert newversion > version, "system has not been upgraded"
        time.sleep(20)


if __name__ == '__main__':
    unittest.main()



