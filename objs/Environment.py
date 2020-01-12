import os

class Environment:

    def __init__(self):
        if os.environ['AWS_PROFILE'] == None:
            raise Exception('There\'s no way to know which profile should be used.')


    def get_region(self) -> str:
        return "us-east-1"
