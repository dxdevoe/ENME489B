# Example Thingspeak code for a channel with 3 feeds

import time
import httplib, urllib
import random

while True:
  params = urllib.urlencode(
    {'field1': random.randrange(100,1000),
     'field2': random.randrange(100,1000),
     'field3': random.randrange(100,1000),
     ‘api_key':"RV3H5FDV17IZNFY7"})         # enter your channel’s write API key

  headers = {"Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"}

  conn = httplib.HTTPConnection("api.thingspeak.com:80")
  conn.request("POST", "/update", params, headers)
  response = conn.getresponse()
  print response.status, response.reason

  time.sleep(16)        # 15 sec min between Thingspeak data
