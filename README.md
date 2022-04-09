
# Info
https://www.youtube.com/watch?v=LgAE41RVZAI

```/bigdata/main.py``` for sending large strings  
```/fake_data/main.py``` for sending data that looks real

# Config
Please see ```.env```

| Key | Default | Info
| - | - | -
| TARGET | https://ping-newdatabase-default-rtdb.firebaseio.com/Userinfo.json | The Target for ```/fake_data/main.py```
| TARGETS | https://ping-newdatabase-default-rtdb.firebaseio.com/Userinfo.json,https://ping-user-default-rtdb.firebaseio.com/OnRequest.json,https://mydatabase-f87de-default-rtdb.firebaseio.com/Userinfo.json | The Targets for ```/bigdata/main.py``` with automatic validation
| THREADS | 4 | Thread count for ```/fake_data/main.py```. Please note that ```/bigdata/main.py``` has a thread for every target!
| FAKE_DATA_URL | https://my.api.mockaroo.com/windowtoolbox | API URL for Fake Data (https://mockaroo.com/)
| API_KEY | 81300f30 | https://mockaroo.com/ API Key

# Install

1. Install requirements: ```pip3 install -r requirements.txt```
2. Run one of the following commands: ```python3 fake_data/main.py``` or ```python3 bigdata/main.py```

# Disclaimer

This is only for educational purposes.

