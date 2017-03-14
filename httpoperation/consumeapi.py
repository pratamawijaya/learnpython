'''
example http request
need requests module

pip install requests
'''

import requests
import json

url = "https://pratamawijaya.com/api/get_recent_posts/?page=1"

t = requests.get(url)
newDictionary=json.loads(t.content.decode('utf-8'))
print(newDictionary['pages'])