from objs.Environment import Environment
from objs.Business import Business
from regions import regions
import botocore

def infos():
    
    environment = Environment()
    awsregion = environment.get_region()
    business = Business()

    for awsregion in regions:
        try:
            business.show_data_from_region(awsregion)
        except botocore.exceptions.ClientError:
            pass