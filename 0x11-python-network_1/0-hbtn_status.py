#!/usr/bin/python3
import urllib.request
"""
 fetches https://alx-intranet.hbtn.io/status
 Using the urllib library
"""


if __name__ == '__main__':
    url_request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(url_request) as response:
        body = response.read()
    print(f'Body response:\n    - type: {type(body)}')
    print(f'    - content: {body}')
    print(f'    - utf8 content: {body.decode("utf-8")}')
