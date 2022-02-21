import pysftp
import paramiko
import glob
import os
import io
import unittest
import pytest
import allure
from test import test_001_Download_Build

class build_download(unittest.TestCase):

    def test_download(self):
        self.launch_site()

    @allure.step("Launch1 site")
    def launch_site(self):
        build = test_001_Download_Build.download
        build.test_downloadn_build(self)

    if __name__ == '__main__':
        unittest.main()
