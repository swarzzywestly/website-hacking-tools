#!/usr/bin/env python
# using python to send a post request to websites.

import requests

target_url = "http://192.168.110.155/dvwa/login.php"
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)
