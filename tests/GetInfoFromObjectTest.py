import sys
import unittest
from raw_environment_data import raw_environment_data
sys.path.append("..")
from objs.EbWrapper import EbWrapper

class GetInfoFromObjectTest(unittest.TestCase):


    def __init__(self, *args, **kwargs):
        super(GetInfoFromObjectTest, self).__init__(*args, **kwargs)
        self.ebWrapper = EbWrapper()
        self.ebWrapper.set_eb_raw_json_data(raw_environment_data)


    def testGetEnvironemntNameFromRawEbData(self):
        self.assertEqual(
            self.ebWrapper.get_environment_name(), 
            "danilocgsilva-me-producao-b"
            )


    def testeGetApplicationNameFromRawEbData(self):
        self.assertEqual(
            self.ebWrapper.get_application_name(),
            "danilocgsilva.me"
        )


    def testGetEnvironmentUrlFromRawEbData(self):
        self.assertEqual(
            self.ebWrapper.get_environment_url(),
            "danilocgsilva-me-producao-b.us-east-1.elasticbeanstalk.com"
        )

if __name__ == '__main__':
    unittest.main()