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

while True:
    threads = []
    for x in range(thread_count):
        threads.append(Sender(x))

    for thread in threads:
        thread.start()