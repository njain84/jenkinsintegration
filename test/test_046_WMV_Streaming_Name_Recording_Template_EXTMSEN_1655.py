from configparser import ConfigParser
from Login_config.LoginHandleradminportal import Loginmsadmin
from selenium import webdriver
from pywinauto.application import Application
import time
from .POM.POM_admin_template import admin_Template
import unittest
from .POM.EPlogin_call import Eplogin
from .POM.EPlogin_callhangup import Ephangup

class WMV_streaming(unittest.TestCase):

    def test_wmv_streaming(self):
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/chromedriver_win32/chromedriver.exe')
        parser = ConfigParser()
        configFilePath = r'C:\PycharmProjects\PycharmProjects\Media_Suite_Smoke\test\config.ini'
        parser.read(configFilePath)
        try:
            time.sleep(2)
            print('Now template')
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            time.sleep(1)
            My_Template.wmv_streaming()
            
            call_to_MS = Eplogin(parser.get('bug_tracker', 'epurl'), driver)
            call_to_MS.EPSIPcall()
            time.sleep(2)
            myloginadmin = Loginmsadmin('admin', 123, parser.get('bug_tracker', 'url'), driver)
            # login the admin portal
            myloginadmin.doLoginadmin()
            driver.implicitly_wait(50)
            stream_name = driver.find_element_by_xpath("//*[@id='call-table-row-0']/td[9]").text
            print('Stream name is', stream_name)
            Value_stream = stream_name.split( )
            final_names = []
            i = 0
            for i in range(0,7):
                if Value_stream[i] == 'wmv1':
                    print('final stream is:',Value_stream[i])
                    final_names.append(Value_stream[i])


                elif Value_stream[i] == 'wmv2':
                    print('final stream is:', Value_stream[i])
                    final_names.append(Value_stream[i])
                i = i+1

            final_names.sort()

            print('final_names', final_names)
            required_value1 = 'wmv1'
            required_value2 = 'wmv2'
            assert final_names[0] == required_value1, 'Test case is failed because name are not wmv1 or wmv2'
            assert final_names[1] == required_value2, 'Test case is failed because name are not wmv1 or wmv2'

        finally:
            print('done')
            driver.quit()
            Hang_up_call = Ephangup(parser.get('bug_tracker', 'epurl'), driver)
            Hang_up_call.doepcallhangup()
            My_Template = admin_Template('driver')
            My_Template.Recording_Template()
            My_Template.disable_WMV_stream()




    if __name__ == '__main__':
        unittest.main()
