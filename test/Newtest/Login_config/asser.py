import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
class Newassert:

    def __init__(self, My_list,driver):
        self.My_list = My_list
        self.driver = driver


    def testName(self):

        test1_var = self.driver.find_elements_by_class_name('table')[0].text
        with open('Temp', 'w') as f1:
            f1.write(test1_var)
        f1 = open('Temp', 'r')
        f1.seek(143)
        self.My_list = f1.read(147-143)
        print(self.My_list)
        assert self.My_list == "H323", "Test case is failed!"


#mylogin = Newassert('My_list')
#mylogin.testName()

        #assert self.My_list == "Detail Call Information", "Test case is failed!"