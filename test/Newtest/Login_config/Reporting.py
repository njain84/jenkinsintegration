import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class loging():
    def __init__(self, driver):
        self.driver = driver

    def Report(self):
        print("click on call button",self.driver.find_elements_by_class_name('panel')[1])
        self.driver.find_elements_by_class_name('panel')[1].click()
        time.sleep(3)
        test1_var = self.driver.find_elements_by_class_name('table')[0].text
        with open('output.txt', 'a') as f1:
            f1.write("\n\n")
            f1.write(test1_var)
        time.sleep(3)  # click on Details, Pop will reflect
        self.driver.find_element_by_id('portalPopoverCall-0').click()
        test_var = self.driver.find_elements_by_class_name('popover')[0].text  # it will save the data

        with open('output.txt', 'a') as f:
            f.write("\n")
            f.write(test_var)

        #time.sleep(3)
        #with open('output.txt') as f:
            #if 'Detail Call Information' in f.read():
                #print("test cases is Passed")
               # test = "Test cases is Passed"
               # with open('output.txt', 'a') as f:
                    #f.write("\n")
                    #f.write(test)

            #else:
                #print("Fail")
                #test = "Test case is Failed"
                #with open('output.txt', 'a') as f:
                    #f.write(test)

