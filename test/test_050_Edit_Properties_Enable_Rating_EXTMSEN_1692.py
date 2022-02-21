import time
import unittest

from selenium.common.exceptions import ElementNotInteractableException

from .POM.Channel import channel
from selenium import webdriver
from Login_config.LoginHandler import Loginms
from configparser import ConfigParser
from .POM.POM_My_media_center import My_Meida_Center

class rating_like_dislike(unittest.TestCase):

    def test_Rating(self):

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
            create_channel.create_channel('like_dislike')
            # It will click on public
            driver.find_element_by_xpath("//*[@id='channelForm']/div[3]/div/label[2]/input").click()
            driver.find_element_by_id('createChannelBtnNext').click()
            time.sleep(2)
            create_channel.select_media()
            #create_channel = channel(driver=driver)
            create_channel.finish()
            # Now admin user will click on like and dislike and will check the this option is working or not



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
            create_channel.check_public_channel('like_dislike')
            time.sleep(3)
            create_channel.click_found_channel()
            # It will play the VoD in channel
            create_channel.play_channel()
            # Now test user will check the like dislike

            driver.find_elements_by_class_name('icon_like')[0].click()
            time.sleep(1)
            count = driver.find_elements_by_class_name('icon_like')[1].text
            print('count is:', count)
            assert count == '1',f'Count should be 1 however it is {count}'
            # it will click on cancel like
            driver.find_elements_by_class_name('icon_like')[1].click()
            time.sleep(1)
            new_count = driver.find_elements_by_class_name('icon_like')[0].text
            print('new_count',new_count)
            assert new_count =='0',f'count should be 0 however it is {count}'
            # it will again click on like
            driver.find_elements_by_class_name('icon_like')[0].click()
            time.sleep(1)
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            # login the userporta2 thru test2
            userportal_login = Loginms('test2', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            # it will check the created channel and will fetch the run time of media file
            create_channel = channel(driver=driver)
            create_channel.check_public_channel('like_dislike')
            time.sleep(3)
            create_channel.click_found_channel()
            # It will play the VoD in channel
            create_channel.play_channel()
            # it will click on dislike
            driver.find_elements_by_class_name('icon_dislike')[0].click()
            time.sleep(1)
            dis_count = driver.find_elements_by_class_name('icon_dislike')[1].text
            print('dislike count:',dis_count)
            assert dis_count == '1', f'count should be 0 however it is {count}'
            # it will login the admin portal to check whether admin can see 1 like and i dislike?
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            userportal_login = Loginms('admin', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            time.sleep(2)
            create_channel = channel(driver=driver)
            create_channel.test_channel()
            create_channel.click_channel()
            create_channel.check_public_channel('like_dislike')
            time.sleep(1)
            create_channel.click_found_channel()
            # it will play the channel
            create_channel.play_channel()
            time.sleep(1)
            # it will count the like thru admin user
            like_count_thru_admin = driver.find_elements_by_class_name('icon_like')[0].text
            print('like_count_thru_admin user is:',like_count_thru_admin)
            assert like_count_thru_admin == '1',f"Like count should be 1 however it is {like_count_thru_admin}"
            time.sleep(1)
            # It will check the dislike count thru admin user
            dislike_count_thru_admin = driver.find_elements_by_class_name('icon_dislike')[0].text
            print('dislike_count_thru_admin_user are:',dislike_count_thru_admin)
            assert dislike_count_thru_admin == '1',f"Dislike count should be 1 however it is {dislike_count_thru_admin}"
            #It will click on like icon
            driver.find_elements_by_class_name('icon_like')[0].click()
            time.sleep(1)
            like_count_admin = driver.find_elements_by_class_name('icon_like')[1].text
            print('Like_count_admin:',like_count_admin)
            assert like_count_admin=='2',f"Like count should be 2 however it is {like_count_admin}"
            time.sleep(1)
            # Below code is to disable the rating in VoD file
            driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
            media_center = My_Meida_Center(driver)
            # login the user portal
            userportal_login = Loginms('admin', '123', parser.get('bug_tracker', 'urluserportal'), driver=driver)
            userportal_login.doLogin()
            time.sleep(2)
            # It will will click to my media center
            media_center.Click_My_Media_Center()
            time.sleep(1)
            media_center.click_edit()
            time.sleep(1)
            media_center.click_edit_properties()
            time.sleep(1)
            media_center.click_enable_rating()
            time.sleep(1)
            media_center.play_Vod()
            # It will verify that rating is disabled or not in the VoD
            time.sleep(1)
            def middle():

                try:
                    # It will click on dislike icon
                    driver.find_element_by_xpath("//*[@id='div_info']/div[1]/div[2]/div[2]/a[3]/i").click()
                except ElementNotInteractableException as e:
                    print('rating is disabled:', e)
                    return e
            verification=middle()
            assert verification != None,"rating is not disablled"

            time.sleep(10)

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
            delete_channel.check_public_channel('like_dislike')
            delete_channel.click_found_channel()
            delete_channel.delete_complete_channel()
            driver.close()

















