#!/usr/bin/python3
import urllib.request
import sys
import urllib.error
"""
urllib.error.HTTPError exceptions and print: Error cod
"""

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            url_response = response.read().decode('utf-8')
            print(url_response)
    except urllib.error.HTTPError as error:
        print(f'Error code: {error.code}')
