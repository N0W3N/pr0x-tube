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
        response = requests.post(url, data=data, headers=headers)

        print(data, response.status_code, response.reason)