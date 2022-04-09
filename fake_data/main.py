from sender import Sender
from dotenv import load_dotenv
from os import getenv
import numpy as np
import requests
import time
import json
import time

load_dotenv()

thread_count = int(getenv('THREADS'))

fake_data_url = getenv('FAKE_DATA_URL')

head = {
    "X-API-Key": getenv('API_KEY')
}

while True:
    fake_data = requests.get(fake_data_url, headers=head, verify=False).text
    fake_data = json.loads(fake_data)

    thread_limit = round(len(fake_data)/thread_count)

    limits = []
    while True:
        if (len(limits) == 0):
            limits.append(thread_limit)
        else:
            limits.append(thread_limit + limits[len(limits)-1])
            if (limits[len(limits)-1] > len(fake_data)):
                limits.pop(len(limits)-1) 
                limits.append(len(fake_data))
                break

    threads = []

    x = 0
    y = 0
    for limit in limits:
        threads.append(Sender(fake_data[x:limit], y))
        print("{}:{}".format(x, limit))
        x = limit
        y = y + 1

    for thread in threads:
        thread.start()