import test_001_H323_Registration_EXTMSEN_1608
import test_003_Registration_with_UDP_EXTMSEN_1606
import test_009_SIP_Registration_TLS_EXTMSEN_1607
import unittest
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
import os
import HtmlTestRunner

current_directory = os.getcwd()
class Report(unittest.TestCase):

    def test_GoogleWiki_Search(self):
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_001_H323_Registration_EXTMSEN_1608.H323),
            unittest.defaultTestLoader.loadTestsFromTestCase(test_003_Registration_with_UDP_EXTMSEN_1606.Temp),
			unittest.defaultTestLoader.loadTestsFromTestCase(test_009_SIP_Registration_TLS_EXTMSEN_1607.TLS)
        ])

        output_file = open(current_directory + "\Smoke test result", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            stream=output_file,
			report_name='Smoke test result',
            report_title='Smoke test result',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner'

        )

        html_runner.run(consolidated_test)

    if __name__ == '__main__':
        unittest.main()