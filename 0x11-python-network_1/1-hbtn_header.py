#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable found
in the header of the response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    url_request = urllib.request.Request(url)
    with urllib.request.urlopen(url_request) as response:
        print(dict(response.headers).get("X-Request-Id"))
