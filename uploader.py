"""Remote Uploader for Mixdrop and other hosters"""

import asyncio
import ssl
import aiohttp
import requests
import re
import csv
import itertools
import os

"""def mixdrop():
    #mixdrop requires mail + api key
    email = "drcreaven@gmail.com"
    url = ''
    key_mixdrop = "TOKEN"
    upload_mixdrop = f'https://api.mixdrop.co/remoteupload?email={email}&key={key_mixdrop}&url={url}'
    mixdrop_r = requests.get(upload_mixdrop)
    mixdrop_response = mixdrop_r.json()
    fileref = mixdrop_response["result"]["fileref"]
    file = requests.get(f'https://api.mixdrop.co/fileinfo?email={email}&key={key_mixdrop}&ref[]= {fileref}')
    file_url = file["result"][]
    print(mixdrop_r.json())"""


def gounlimited():
    """gounlimited only requires an api key, but has its own way to deal with file cloning.
    file code equals everything after the last slash of the video url - generate it with regex"""
    key_gounlimited = 'TOKEN'
    import csv_m

    """opens csv after csv to retrieve the old existing stream-link, parses it through the GO API
            then retrieves the stream link of the new uploaded video and prints it."""

    old_link = (''.join(csv_m.rows[4]))
    file_code = ''.join(re.findall('[^\/]+$', old_link))
    print(file_code)
    upload_gounlimited = f'https://api.gounlimited.to/api/file/clone?key={key_gounlimited}&file_code={file_code}'
    gounlimited_r = requests.get(upload_gounlimited)
    go_response = gounlimited_r.json()
    print(go_response)
    go_vid_url = go_response["result"]["filecode"]
    print(go_vid_url)
    return go_vid_url
