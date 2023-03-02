from threading import Thread
from time import sleep
import requests
import json
import random
import string


def random_string_generator(str_size):
    return ''.join(random.choice(string.ascii_letters + string.punctuation) for x in range(str_size))


class Sender(Thread):
    def __init__(self, target, id):
        super(Sender, self).__init__()
        self.id = id
        self.target = target

    def run(self):
        while True:
            mock_data = {
                "as": random_string_generator(8192),
                "city": random_string_generator(8192),
                "country": random_string_generator(8192),
                "countryCode": random_string_generator(8192),
                "isp": random_string_generator(8192),
                "lat": random_string_generator(8192),
                "lon": random_string_generator(8192),
                "org": random_string_generator(8192),
                "query": random_string_generator(8192),
                "region": random_string_generator(8192),
                "regionName": random_string_generator(8192),
                "status": "success",
                "timezone": random_string_generator(8192),
                "zip": random_string_generator(8192)
            }

            try:
                response = requests.post(self.target, data=json.dumps(mock_data)).text
                print("[{}] {}".format(self.id, response))
            except Exception as e:
                sleep(10)
