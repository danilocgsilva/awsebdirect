class Iterator:

    def set_client_response(self, client_response: dict):
        self.client_response = client_response
        return self


    def count(self):
        return len(self.client_response['Environments'])
