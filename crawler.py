#!/user/bin/env python

# sending a GET Requests to web servers.

import requests

url = "google.com"
try:
    get_response = requests.get("http://" + url)
    print(get_response)
except requests.exceptions.ConnectionError:
    pass
