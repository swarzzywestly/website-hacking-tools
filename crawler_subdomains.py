#!/usr/bin/env python

# Discovering website subdomains

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass
target_url = "http://192.168.110.155/mutillidae/"

with open ("/root/Downloads/subdomains-wodlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomains -->"  + test_url)
