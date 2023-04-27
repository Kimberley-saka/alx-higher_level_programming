#!/usr/bin/python3
"""
Sends post request
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    response = requests.post(url, data)
    try:
        json_res = response.json()
        if json_res:
            print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
