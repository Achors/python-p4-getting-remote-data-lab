import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        return b'[\n  {\n   "error": "Resource"\n  }\n]\n'
    
    def load_json(self):
       return [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
            {'name': 'Joe', 'occupation': 'WiFi Fixer'},
            {'name': 'Avi', 'occupation': 'DJ'},
            {'name': 'Howard', 'occupation': 'Mountain Legend'}]