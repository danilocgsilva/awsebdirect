from objs.Arguments import Arguments
from objs.Environment import Environment
import boto3

arguments = Arguments()
environment = Environment()
eb = boto3.client('elasticbeanstalk', environment.get_region())
response = eb.describe_environments()
for item in response['Environments']:
    app_name = response['Environments'][item]['ApplicationName']
    env_name = response['Environments'][item]['EnvironmentName']
    print(app_name)
    print(env_name)

print('The first argument is ' + arguments.get_argument())
