#!/usr/bin/python3
import urllib.request
import sys
import urllib.error
"""
urllib.error.HTTPError exceptions and print: Error cod
"""

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
