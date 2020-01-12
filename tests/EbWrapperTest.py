import sys
import unittest
from raw_environment_data import raw_environment_data
sys.path.append("..")
from objs.EbWrapper import EbWrapper


class EbWrapperTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(EbWrapperTest, self).__init__(*args, **kwargs)
        self.ebWrapper = EbWrapper()


    def testGetEnvironemntNameFromRawEbData(self):
        self.ebWrapper.set_eb_raw_json_data(raw_environment_data)
        self.assertEqual(
            self.ebWrapper.get_environment_name(), 
            "danilocgsilva-me-producao-b"
            )


    def testeGetApplicationNameFromRawEbData(self):
        self.ebWrapper.set_eb_raw_json_data(raw_environment_data)
        self.assertEqual(
            self.ebWrapper.get_application_name(),
            "danilocgsilva.me"
        )


    def testGetEnvironmentUrlFromRawEbData(self):
        self.ebWrapper.set_eb_raw_json_data(raw_environment_data)
        self.assertEqual(
            self.ebWrapper.get_environment_url(),
            "danilocgsilva-me-producao-b.us-east-1.elasticbeanstalk.com"
        )


    def testSetEbRawJsonData(self):
        with self.assertRaises(TypeError):
            self.ebWrapper.set_eb_raw_json_data("It is not a dict")


if __name__ == '__main__':
    unittest.main()