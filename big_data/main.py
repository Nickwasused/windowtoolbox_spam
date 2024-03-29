from sender import Sender
from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()

targets = getenv('TARGETS').split(",")
tmp_targets = []
for target in targets:
    if requests.get(target, verify=False).status_code == 200:
        tmp_targets.append(target)
print(tmp_targets)
targets = tmp_targets

while True:
    threads = []
    x = 0
    for target in targets:
        threads.append(Sender(target, x))
        x = x + 1
        
    if len(targets) == 0:
        break

    for thread in threads:
        thread.start()