import requests
from Test_Data_Extractor import *
class API_Client:
    def __init__(self):
        test_data = TestDataExtractor()
        self.config = test_data.get_data_from_test_data()
        self.baseurl = self.config["baseurl"]
        self.headers = self.config["headers"]

    def send_request(self, method, endpoint, payload=None, params=None):
        url = f"{self.baseurl}{endpoint}"
        response = requests.request(method, url, json=payload, headers=self.headers, params=params)
        return response

    def send_request_form_data_urlencoded(self, method, endpoint, payload=None, params=None, form_data=None):
        self.headers = self.config["headers_form_data_urlencoded"]
        url = f"{self.baseurl}{endpoint}"
        response = requests.request(method, url, json=payload, headers=self.headers, params=params, data=form_data)
        return response

    def send_request_form_data(self, method, endpoint, file,payload=None, params=None):
        self.headers = self.config["headers_form_data"]
        url = f"{self.baseurl}{endpoint}"
        response = requests.request(method, url, json=payload, headers=self.headers, params=params, files =file)
        return response



