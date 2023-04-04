#!/usr/bin/python3
import urllib.request
import sys
import urllib.parse
"""
Send a post request with an email as a parameter
"""


url = sys.argv[1]
email = sys.argv[2]

if __name__ == "__main__":
    post_email = urllib.parse.urlencode({'email': email})
    data = post_email.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        url_response = response.read().decode('utf-8')
        print(f'{url_response}')
