#!/usr/bin/python3
import urllib.request
import sys
import urllib.parse
"""
Send a post request with an email as a parameter
"""


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        url_response = response.read().decode('utf-8')
        print(f'{url_response}')
