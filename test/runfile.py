import unittest
unittest.TestLoader.sortTestMethodsUsing = lambda self,a,b:(a>b)-(a>b)

class SampleTest(unittest.Testcase):

    def test_001_H323_Registration_EXTMSEN_1608(self):
        print('run')

    if __name__ == '__main__':
        unittest.main()
