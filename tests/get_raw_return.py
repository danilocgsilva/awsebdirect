import sys
sys.path.append('..')
from objs.Environment import Environment
import boto3

environment = Environment()
eb = boto3.client('elasticbeanstalk', environment.get_region())
print(eb.describe_environments())