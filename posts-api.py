import mezzanine_api
import subprocess
import json

file_number = 1


with open('test%s.json' % file_number, 'r') as f:
    file_number += 1
    data = json.load(f)
    print(data["Site"][0]["title"])
    print(data["Site"][1]["description"])
    print(data["Site"][2]["category"])
