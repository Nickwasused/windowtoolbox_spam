import requests
import time
import json


fake_data_url = "https://my.api.mockaroo.com/window"
target_firebase = "https://ping-newdatabase-default-rtdb.firebaseio.com/Userinfo.json"

head = {
    "X-API-Key": "81300f30"
}

fake_data = requests.get(fake_data_url, headers=head, verify=False).text
fake_data = json.loads(fake_data)

print(len(fake_data))

for item in fake_data:
    myobj = {
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

    x = requests.post(target_firebase, data = json.dumps(myobj))
    print(x.text)