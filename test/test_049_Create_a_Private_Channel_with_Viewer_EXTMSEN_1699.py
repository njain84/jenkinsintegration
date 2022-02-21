import time
import unittest
from .POM.Channel import channel
from selenium import webdriver
from Login_config.LoginHandler import Loginms
from configparser import ConfigParser

class create_a_private_channel(unittest.TestCase):

    def test_private_channel(self):
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
            create_channel.create_channel('private_channel')
            # It will click on public
            #driver.find_element_by_xpath("//*[@id='channelForm']/div[3]/div/label[2]/input").click()
            driver.find_element_by_id('createChannelBtnNext').click()
            time.sleep(2)
            create_channel.select_media()
            driver.implicitly_wait(2)
            create_channel.drop_down()
            # it will add the user
            create_channel.add_name('test1')
            time.sleep(1)
            create_channel.finish()
            #print('Now need to login user portal with test user')
            time.sleep(1)
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')

            # login the userportal
            userportal_login = Loginms('test1', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            # it will check the created channel and will fetch the run time of media file
            create_channel = channel(driver=driver)
            # it will check whether test1 user can see the private channel or not.expectation is user should be
            #able to see this
            create_channel.check_public_channel('private_channel')
            create_channel.click_found_channel()
            run_time = create_channel.play_channel()
            print('value is', run_time)
            assert run_time >= '00:04', f"File is not being played,current time is {run_time}" \
                                        f" but it should be more than or equal to 4."
            # login the userportal with test2 user and user should not be able to watch the channel
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            userportal_login = Loginms('test2', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            # it will check the created channel and will fetch the run time of media file
            create_channel = channel(driver=driver)
            # it will check whether test2 user can see the private channel or not.expectation is user should not be
            # able to see this
            # output will store the return value which will tell option ALL is available or not
            # Option all is None means option All is available
            option_all = create_channel.check_option_all()
            print('Option All is;',option_all)
            if option_all == None:
                create_channel.check_public_channel('private_channel')
                file_existence = driver.find_elements_by_class_name('div_nocontent_txt')[1].text
                print('file is:', file_existence)
                assert file_existence == 'No Search Results.', 'user can see the private file'
            else:
                print('Test case is passed')
                assert option_all == 'All is not available and it means user can not see file', 'user can see the private file'
        finally:
            parser = ConfigParser()
            parser.read('config.ini')
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            userportal_login = Loginms('admin', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            # it will delete the created channel
            delete_channel = channel(driver=driver)
            time.sleep(2)
            delete_channel.test_channel()
            delete_channel.click_channel()
            delete_channel.check_public_channel('private_channel')
            delete_channel.click_found_channel()
            delete_channel.delete_complete_channel()
            driver.close()
