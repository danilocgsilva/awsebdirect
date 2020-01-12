from objs.EbWrapper import EbWrapper

class Talk:

    def show_data(self, ebWrapper: EbWrapper, awsregion: str):
        print('--- ENVIRONMENT NAME: ' + ebWrapper.get_environment_name() + ' ---')
        print("Application name: " + ebWrapper.get_environment_name())
        print("Environment url: " + ebWrapper.get_environment_url())
        print("Environment id: " + ebWrapper.get_environment_id())
        print("Environment status: " + ebWrapper.get_status())
        print("Region: " + awsregion)

    def show_environments_in_region(self, region: str, counted: int):
        print("In the region " + region + ", you have " + str(counted) + " environments.")

    def show_regions_count(self, counted: int):
        print('There are ' + str(counted) + ' environments in your whole AWS account.')