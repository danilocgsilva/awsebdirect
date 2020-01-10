from objs.Arguments import Arguments
from objs.Environment import Environment
from objs.EbWrapper import EbWrapper
import boto3

arguments = Arguments()
environment = Environment()
awsregion = environment.get_region()
eb = boto3.client('elasticbeanstalk', awsregion)
response = eb.describe_environments()

for item in response['Environments']:
    
    ebWrapper = EbWrapper()
    ebWrapper.set_eb_raw_json_data(item)

    print('--- ENVIRONMENT NAME: ' + ebWrapper.get_environment_name() + ' ---')
    print("Application name: " + ebWrapper.get_environment_name())
    print("Environment url: " + ebWrapper.get_environment_url())

print("")
print("The data has been fetched from the region " + awsregion + ".")
