import os
from selenium import webdriver
import webbrowser
import pyautogui
import time
#from PIL import ImageGrab
import base64
#it will take screen shot of first page of report
import unittest
import subprocess

class Screen(unittest.TestCase):

    def test_screenshot(self):
        new = 2
        #url = "C:/Users/MediaSuite/Desktop/Microsoft Edge
        #url = "file:///C:/Jenkins/workspace/MS_smoke(VM1)/allure-report/index.html"
        #webbrowser.open(url, new=new)
        subprocess.call([r'C:/PycharmProjects/PycharmProjects/Media_Suite_Smoke/test/Report_email/report_open.bat'])
        time.sleep(6)
        screenshot = pyautogui.screenshot()
        time.sleep(2)
        screenshot.save("C:/Jenkins/workspace/for_report_transfer/Report_screen.png")
        #time.sleep(10)
        #box = (10, 60, 1090, 810)
        #box = (50, 90, 950, 600)
        #ImageGrab.grab().crop(box).save("C:/Jenkins/workspace/for_report_transfer/Report_screen.png", "JPEG")

    # need to convert image
    # base64Img = ''

    # with open("C:/Jenkins/workspace/MS_smoke/screenshot2.png", "rb") as imageFile:
    # base64Img = base64.b64encode(imageFile.read())

    # with open("C:/Jenkins/workspace/MS_smoke/screenshot2.html", "wb+") as writer:
    # writer.write('<img src="data:image/png;base64,'.encode())
    # writer.write(base64Img)
    # writer.write('">'.encode())
    # writer.close()

    if __name__ == '__main__':
        unittest.main()
