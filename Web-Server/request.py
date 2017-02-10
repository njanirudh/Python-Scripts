import requests
import json

#  Setting the URL and Payload for the request
url = 'http://192.168.0.17:5000/speechRecog/'
payload = {'key1': 'value1', 'key2': 'value2'}

"""
# GET
r = requests.get(url)


# GET with params in URL
r = requests.get(url, params=payload)
"""

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON
r = requests.post(url, data=json.dumps(payload))

# Response, status etc
print r.text
print r.status_code
print r.url