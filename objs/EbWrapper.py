class EbWrapper:

    def set_eb_raw_json_data(self, eb_raw_json_data: dict):

        if not type(eb_raw_json_data).__name__ == 'dict':
            raise TypeError('The entered data must be of type dict')

        self.eb_raw_json_data = eb_raw_json_data
        return self


    def get_environment_name(self):
        return self.eb_raw_json_data['EnvironmentName']


    def get_application_name(self):
        return self.eb_raw_json_data['ApplicationName']


    def get_environment_url(self):
        return self.eb_raw_json_data['CNAME']

