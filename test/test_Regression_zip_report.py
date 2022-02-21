import os
import zipfile
import shutil
import unittest

class ZIP(unittest.TestCase):

    def test_zipdir(self):
        # ziph is zipfile handle
        shutil.make_archive('C:/Jenkins/workspace/Regression/allure-report', 'zip','C:/Jenkins/workspace/Regression/allure-report')

        original = r'C:\Jenkins\workspace\Regression/allure-report.zip'
        target = r'C:\jenkins\workspace\Regression_report\allure-report.zip'

        shutil.move(original, target)

    if __name__ == '__main__':
        unittest.main()
