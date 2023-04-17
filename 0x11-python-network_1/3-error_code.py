#!/usr/bin/python3
import urllib.request
import sys
import urllib.error
"""
urllib.error.HTTPError exceptions and print: Error cod
"""

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(esponse.read().decode('ascii'))
    except urllib.error.HTTPError as error:
        print(f'Error code: {error.code}')
