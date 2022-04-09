from threading import Thread
from time import sleep
import requests
import json
import random
import string

class Sender(Thread):
    def __init__(self, target, id):
        super(Sender, self).__init__()
        self.id = id
        self.target = target
        
    def random_string_generator(self, str_size):
        return ''.join(random.choice(string.ascii_letters + string.punctuation) for x in range(str_size))

    def run(self):
        while True:
            mock_data = {
                "as": self.random_string_generator(8192),
                "city": self.random_string_generator(8192),
                "country": self.random_string_generator(8192),
                "countryCode": self.random_string_generator(8192),
                "isp": self.random_string_generator(8192),
                "lat": self.random_string_generator(8192),
                "lon": self.random_string_generator(8192),
                "org": self.random_string_generator(8192),
                "query": self.random_string_generator(8192),
                "region": self.random_string_generator(8192),
                "regionName": self.random_string_generator(8192),
                "status": "success",
                "timezone": self.random_string_generator(8192),
                "zip": self.random_string_generator(8192)
            }

            try:
                response = requests.post(self.target, data = json.dumps(mock_data)).text
                print("[{}] {}".format(self.id, response))
            except:
                sleep(10)

