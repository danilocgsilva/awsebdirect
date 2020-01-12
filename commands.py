from objs.Environment import Environment
from objs.Business import Business
from objs.Iterator import Iterator
from objs.Talk import Talk
from regions import regions
import botocore
import boto3

def infos():
    
    environment = Environment()
    awsregion = environment.get_region()
    business = Business()

    for awsregion in regions:
        try:
            business.show_data_from_region(awsregion)
        except botocore.exceptions.ClientError:
            pass


def count():

    iterator = Iterator()

    talk = Talk()

    for awsregion in regions:
        ebClient = boto3.client('elasticbeanstalk', awsregion)

        try:
            region_response = ebClient.describe_environments()
        except botocore.exceptions.ClientError:
            print("Error on fetching data from region " + awsregion + ". Sorry!")
            continue

        iterator.set_client_response(region_response)

        talk.show_environments_in_region(awsregion, iterator.count())
