import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class Loginmsadmin:
    def __init__(self, loginUsername, loginPassword, url:str, driver):
        print("Constructor of Login Handler")
        self.username = loginUsername
        self.password = loginPassword
        self.url = url
        self.driver = driver

    def doLoginadmin(self):
        print("do login Method called :", self.username)
        self.driver.get(self.url)
        time.sleep(5)
        print("Hi")
        self.driver.find_element_by_id('loginForm:userName').send_keys(self.username)
        print("Hi")
        time.sleep(3)
        self.driver.find_elements_by_class_name('form-control')[1].send_keys(self.password)
        print(self.driver.find_elements_by_class_name('btn')[0])
        time.sleep(5)
        self.driver.find_elements_by_class_name('btn')[1].click()
        print(self.driver.find_elements_by_id('dialOutButton'))