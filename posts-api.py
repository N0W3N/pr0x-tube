import json
import requests
import sys
import csv

file_number = 2

while True:
    with open('test%s.csv' % file_number, 'r', newline='') as parser:
        file_number += 1
        content = csv.reader(parser, delimiter=' ')
        rows = list(content)
        title = str(rows[0])
        content = str(rows[1])
        category = str(rows[2])

        url = 'http://127.0.0.1:8000/api/posts'

        data = json.dumps({
            "title": title,
            "content": content,
            "categories": category,
            "status": 1,
        })
        headers = {'Content-type': 'application/json',
                   'Authorization': 'Token TEST'}
        try:
            response = requests.post(url, data=data, headers=headers)
        except ConnectionError:
            print("Failed to establish a new connection.\n"
                  f"Details: {ConnectionError}")
        except ConnectionRefusedError as CRE:
            print("Connection has been refused. Token is either invalid or doesn't exist.\n"
                  f"Details: {CRE}")
        else:
            print()
