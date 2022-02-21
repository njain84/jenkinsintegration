import webbrowser
import requests
import tkinter as tk
import time
from selenium import webdriver
class Loginms:
    def __init__(self, loginUsername, loginPassword, url: str, driver):
        print("Constructor of Login Handler")
        self.username = loginUsername
        self.password = loginPassword
        self.url = url
        self.driver = driver

    def doLogin(self):
        print("do login Method called :", self.username)
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element_by_id('login_user').send_keys(self.username)
        print("Hi")

        print(self.driver.find_elements_by_class_name('form-control')[1])
        self.driver.find_elements_by_class_name('form-control')[1].send_keys(self.password)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/input').send_keys(1234)
        time.sleep(5)
        print(self.driver.find_elements_by_class_name('btn')[0])
        self.driver.find_elements_by_class_name('btn')[0].click()
