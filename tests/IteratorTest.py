import unittest
import sys
from raw_eb_cli_response import raw_eb_cli_response
sys.path.append("..")
from objs.Iterator import Iterator

class IteratorTest(unittest.TestCase):

    def testCanCountEnvironmentFromEbCliResponse(self):
        iterator = Iterator()
        iterator.set_client_response(raw_eb_cli_response)
        counted_environments = iterator.count()
        self.assertEqual(1, counted_environments)


if __name__ == '__main__':
    unittest.main()