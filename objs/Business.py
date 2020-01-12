from objs.EbWrapper import EbWrapper
from objs.Talk import Talk
import boto3

class Business:

    def show_data_from_region(self, awsregion: str):

        self.__get_data_from_region__(awsregion)

        for eb_env_data in self.region_response['Environments']:
            ebWrapper = EbWrapper()
            ebWrapper.set_eb_raw_json_data(eb_env_data)
            talk = Talk()
            talk.show_data(ebWrapper, awsregion)

    
    def __get_data_from_region__(self, region):
        ebClient = boto3.client('elasticbeanstalk', region)
        self.region_response = ebClient.describe_environments()
