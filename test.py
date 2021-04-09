import json
from datetime import datetime
with open('config.json','r') as c:
    params = json.load(c)["params"]

#print(params['web_name'])
#print(params['web_subname'])
#print(params['fb_url'])
print(datetime.now())

