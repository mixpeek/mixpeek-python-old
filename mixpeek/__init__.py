import requests
import os
from urllib.parse import urlencode
import json


class Mixpeek:
    def __init__(self, api_key, access_key=None, secret_key=None, region=None):
        self.base_url = "https://api.mixpeek.com/v1"
        self.header = {"Authorization": api_key}
        # optional params if user is using AWS S3
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region

    def index(self, file_path, **payload):
        """
        upload your file to the mixpeek server for extraction
        params:
        file_path: str - path to file

        payload: dict - optional params
            user_id: str - for user level filtering in search
            tags: str - tags associated with file
            static_file_url: str - reference for file
        """
        # build api endpoint url with key and path
        url = f'{self.base_url}/file/index-one'
        # get filename from path
        filename = os.path.basename(file_path)
        # file upload
        files = [
            ('file', (filename, open(file_path, 'rb'), 'application/octet-stream'))
        ]
        # send request
        response = requests.request(
            "POST", url, headers=self.header, data=payload, files=files)
        return response.json()

    def index_bucket(self, bucket):
        # build api endpoint url with key and path
        url = f'{self.base_url}/file/index-many'
        # add url params
        payload = json.dumps({
            "s3_bucket": bucket,
            "aws_access_key": self.access_key,
            "aws_secret_key": self.secret_key,
            "region": self.region
        })
        # send request
        response = requests.request(
            "POST", url, headers=self.header, data=payload)
        return response.json()

    def search(self, query, **params):
        """
        search your indexed files
        query: str - query string

        params: dict - optional params
            context: str - include context in response
            tags: str - filter by tags
            user-id: str - for user level filtering in search
        """
        url = f'{self.base_url}/search'
        # add url params
        url_params = urlencode(params)
        # build full url
        full_url = "{}?q={}&{}".format(url, query, url_params)
        # send request
        response = requests.request(
            "GET", full_url, params=params, headers=self.header)

        return response.json()
