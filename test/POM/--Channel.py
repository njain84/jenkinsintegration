from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
class channel():


    def __init__(self, driver):
        print("Constructor of End point Login Handler")
        self.driver = driver

    def test_channel(self):
        self.driver.implicitly_wait(2)
        # it will go to My media center
        self.driver.find_elements_by_class_name('avatar_active')[0].click()
        WebDriverWait(self.driver, 2)
        self.driver.find_elements_by_class_name('btn')[2].click()
    def click_channel(self):
        #WebDriverWait(self.driver, 2)
        time.sleep(2)
        self.driver.find_elements_by_class_name('ng-binding')[14].click()
    def create_channel(self,channel_name):
        print("create")
        time.sleep(2)
        #self.driver.find_element_by_link_text("Create a new channel").click()
        try:
            self.driver.find_element_by_link_text("Create Channel").click()
        except NoSuchElementException as e:
            print('It will try another method to create channel due to error:',e)
            try:
                print('trying 2nd method')
                self.driver.find_element_by_link_text("Create a new channel").click()
            except NoSuchElementException as e:
                print('still error:', e)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_name('name').send_keys(channel_name)
    def select_media(self):
        self.driver.find_element_by_xpath("//*[@id='firstModal']/div/div/div[2]/div/div/div[4]/div/div[1]/ng-include/div/div[6]/vcm-archive-list/div/div[7]/div/div[1]/div[2]/span[4]").click()
        time.sleep(1)
        #it will click on next
        self.driver.find_element_by_id('createChannelBtnNext').click()
        print('selected media')
        time.sleep(1)

    def drop_down(self):

        try:
            # it will select viewer
            # self.driver.find_elements_by_class_name('form-control')[6].click()
            self.select = Select(self.driver.find_elements_by_class_name('form-control')[6])
            self.select.select_by_visible_text('Viewer')
        except Exception as e:
            self.select = Select(self.driver.find_elements_by_class_name('form-control')[8])
            self.select.select_by_visible_text('Viewer')
    # it will add the name
    def add_name(self,name):
        self.driver.find_element_by_name('addChannelMember').send_keys(name)
        time.sleep(3)
        quantity_element = self.driver.find_element_by_name('addChannelMember')
        quantity_element.send_keys(Keys.ARROW_DOWN)
        quantity_element.send_keys(Keys.ENTER)
        # It will add the user by clicking on Add button
        self.driver.find_elements_by_class_name('col-sm-1')[0].click()

    def finish(self):

        # it will finish
        self.driver.find_element_by_id('createChannelBtnNext').click()
        print('finished')

    def check_option_all(self):

        try:
            time.sleep(2)
            self.driver.find_element_by_link_text('All').click()
        except NoSuchElementException as e:
            print('All is not available')
            All_not = 'All is not available and it means user can not see file'
            return All_not

    def check_public_channel(self,channel_name):
        # It will check public/private channel existence.
        time.sleep(3)
        print('it is in check public channel')
        # Calling another function below
        channel.check_option_all(self)

        # self.driver.find_elements_by_class_name('firstlink')[0].click()
        print('will run or not')
        time.sleep(2)
        #self.driver.implicitly_wait(3)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys(channel_name)
        print('put the name')
        time.sleep(5)
        # it will click on search icon
        self.driver.find_elements_by_class_name('glyphicon')[1].click()
        print('select the channel')
        time.sleep(2)

    def click_found_channel(self):
        # It will click on found channel    /html/body/div[2]/div[3]/div[2]/div[4]/div/div/div[5]/div/div[2]/div[1]/b
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[5]/div/div[2]/div[1]/b").click()

        except NoSuchElementException as e:
            print('error:',e)
            print('excepted')
            self.driver.find_elements_by_class_name('ng-binding')[58].click()
            print('excepted1')

    def play_channel(self):
        # It will play the file
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[5]/vcm-archive-list/div/div[3]/div/div[1]/div[2]/div[1]/div/div/a/img").click()
        time.sleep(10)
        # it will move the cursor to get the run time
        act = ActionChains(self.driver)
        print('played the file')
        act.move_by_offset(258,454).perform()
        print('moved')
        #it will capture the current run time of file
        current_time=self.driver.find_elements_by_class_name('current_time')[0].text
        print('current time is:')
        return(current_time)
    def delete_complete_channel(self):

        time.sleep(2)
        self.driver.find_elements_by_class_name('icon_only')[1].click()
        self.driver.implicitly_wait(2)
        self.driver.find_elements_by_class_name('btn')[1].click()
        time.sleep(1)











