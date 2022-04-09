from dotenv import load_dotenv
from threading import Thread
from os import getenv
import requests
import json

load_dotenv()

target_firebase = getenv('TARGET')

class Sender(Thread):
    def __init__(self, data, id):
        super(Sender, self).__init__()
        self.data = data
        self.id = id
        
    def run(self):
        data = self.data

        for item in data:
            mock_data = {
                "as": item["as"],
                "city": item["city"],
                "country": item["country"],
                "countryCode": item["country_code"],
                "isp": item["isp"],
                "lat": item["lat"],
                "lon": item["long"],
                "org": item["org"],
                "query": item["query"],
                "region": item["region"],
                "regionName": item["regionname"],
                "status": "success",
                "timezone": item["timezone"],
                "zip": item["zip"]
            }

            response = requests.post(target_firebase, data = json.dumps(mock_data)).text
            print("[{}] {}".format(self.id, response))

