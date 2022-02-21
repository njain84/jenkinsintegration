import os
import zipfile
import shutil
import unittest

class ZIP(unittest.TestCase):

    def test_zipdir(self):
        # ziph is zipfile handle
        shutil.make_archive('C:/Jenkins/workspace/MS_smoke(VM1)/allure-report', 'zip','C:/Jenkins/workspace/MS_smoke(VM1)/allure-report')

        original = r'C:\Jenkins\workspace\MS_smoke(VM1)/allure-report.zip'
        target = r'C:\Jenkins\workspace\for_report_transfer\allure-report.zip'

        shutil.move(original, target)

    if __name__ == '__main__':
        unittest.main()
