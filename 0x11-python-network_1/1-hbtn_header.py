#!/usr/bin/python3
import sys
import urllib.request
"""
Displays the value of the X-Request-Id variable found
in the header of the response
"""



url = sys.argv[1]
url_request = urllib.request.Request(url)
with urllib.request.urlopen(url_request) as response:
    url_response = response.info()
    print(f'{url_response.get("X-Request-Id")}')
