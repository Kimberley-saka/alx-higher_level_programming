#!/usr/bin/python3
import urllib.request
"""
 fetches https://alx-intranet.hbtn.io/status
 Using the urllib library
"""


url_request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(url_request) as response:
    body = response.read()
    print(f'Body response:')
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
    print(f'\t- utf8 content: {body.decode("utf-8")}')
