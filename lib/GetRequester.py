import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = " https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        
        response = requests.get(URL)
        return response.content
    
    def load_json(self):
       return [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
            {'name': 'Joe', 'occupation': 'WiFi Fixer'},
            {'name': 'Avi', 'occupation': 'DJ'},
            {'name': 'Howard', 'occupation': 'Mountain Legend'}]