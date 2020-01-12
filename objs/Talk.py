from objs.EbWrapper import EbWrapper

class Talk:

    def show_data(self, ebWrapper: EbWrapper, awsregion: str):
        print('--- ENVIRONMENT NAME: ' + ebWrapper.get_environment_name() + ' ---')
        print("Application name: " + ebWrapper.get_environment_name())
        print("Environment url: " + ebWrapper.get_environment_url())
        print("Region: " + awsregion)