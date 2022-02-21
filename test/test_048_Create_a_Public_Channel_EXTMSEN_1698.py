import time
import unittest
from .POM.Channel import channel
from selenium import webdriver
from Login_config.LoginHandler import Loginms
from configparser import ConfigParser

class create_a_public_channel(unittest.TestCase):

    def test_public_channel(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe',options=options)
            userportal_login = Loginms('admin', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            time.sleep(2)
            create_channel = channel(driver=driver)
            create_channel.test_channel()
            create_channel.click_channel()
            create_channel.create_channel('public_channel')
            # It will click on public
            driver.find_element_by_xpath("//*[@id='channelForm']/div[3]/div/label[2]/input").click()
            driver.find_element_by_id('createChannelBtnNext').click()
            time.sleep(2)
            create_channel.select_media()
            create_channel.finish()
            #create_channel = channel(driver=driver)
            print('Now need to login user portal with test user')
            time.sleep(1)
            #driver.close()
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            #time.sleep(2)
            #login the userportal
            userportal_login = Loginms('test1', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            # it will check the created channel and will fetch the run time of media file
            create_channel = channel(driver=driver)
            create_channel.check_public_channel('public_channel')
            create_channel.click_found_channel()
            run_time = create_channel.play_channel()
            print('value is',run_time)
            assert run_time >= '00:04', f"File is not being played,current time is {run_time}" \
                                                        f" but it should be more than or equal to 4."
            print('start')
        finally:
            parser = ConfigParser()
            configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
            parser.read(configFilePath)
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            userportal_login = Loginms('admin', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            # it will delete the created channel
            delete_channel = channel(driver=driver)
            time.sleep(2)
            delete_channel.test_channel()
            delete_channel.click_channel()
            delete_channel.check_public_channel('public_channel')
            delete_channel.click_found_channel()
            delete_channel.delete_complete_channel()
            driver.close()











