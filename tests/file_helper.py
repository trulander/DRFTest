import os

class Session:
    def close(self):
        print("Closed session")

class Api:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = Session()

    def request(self, method, data):
        print('Executed', method)

    def close(self):
        print("Closing session")
        self.session.close()

class FileHelper:

    def __init__(self, api: Api):
        self.api = api
        # self.logger = logger

    def remove_file(self, filepath):
        if os.path.isfile(filepath):
            # self.logger.info("removing file %s", filepath)
            print(f"removing file  {filepath}")
            os.unlink(filepath)
        else:
            print('file no exist')

    def prepare_file(self, filepath):
        # self.logger.info("Preparing file %s for upload", filepath)
        print("Preparing file %s for upload", filepath)
        return bytes()

    def upload_file(self, filepath):
        data = self.prepare_file(filepath=filepath)
        self.api.request("POST", data)