import os
import zipfile
import shutil
import unittest
import allure
import pytest
from test import test_Regression_zip_report


class ZIP1(unittest.TestCase):

    def test_zipdir1(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        folder = test_Regression_zip_report.ZIP

        folder.test_zipdir(self)

    if __name__ == '__main__':
        unittest.main()
