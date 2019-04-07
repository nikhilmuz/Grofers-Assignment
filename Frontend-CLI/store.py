#!/usr/bin/env python
import sys
import requests
import time

API_BASE = "http://localhost:8000/"
command = sys.argv[1]
if command == 'get':
    key = sys.argv[2]
    url = API_BASE + "get/"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"key\"\r\n\r\n" + key + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        json = response.json()
        print(json['value'])
    elif response.status_code == 404:
        print("Key Not Found")
    else:
        print("Error")
elif command == 'put':
    key = sys.argv[2]
    value = sys.argv[3]
    url = API_BASE + "update/"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"key\"\r\n\r\n" + key + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"value\"\r\n\r\n" + value + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        json = response.json()
        print("Successfully Updated Key")
    else:
        print("Error")
elif command == 'watch':
    url = API_BASE + "time/"

    payload = ""
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    if response.status_code == 200:
        timestamp = response.json()['time']
        url = API_BASE + "watch/"
        while True:
            payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
                      "name=\"time\"\r\n\r\n"+timestamp+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW-- "
            headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'cache-control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            if response.status_code == 200:
                timestamp = response.json()['last']
                count = response.json()['count']
                for i in range(count):
                    print("Key: " + response.json()['result'][i]['key'] + " Value: " + response.json()['result'][i]['value'])
            time.sleep(0.5)
    else:
        print("Error")
else:
    print("Invalid Syntax")
