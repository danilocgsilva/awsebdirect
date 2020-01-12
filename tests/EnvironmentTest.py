import os
import sys
import unittest
sys.path.append('..')
from objs.Environment import Environment

class EnvironmentTest(unittest.TestCase):

    def testThrowExceptionIfNoAwsProfileSetted(self):

        if os.environ.get('AWS_PROFILE') != None:
            del os.environ['AWS_PROFILE']

        with self.assertRaises(Exception):
            Environment()


if __name__ == '__main__':
    unittest.main()