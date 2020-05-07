"""Remote Uploader for Mixdrop and other hosters.
It takes the grabbed (current) streaming link and reuploads/clones it into our own account.
pr0x-tube uses this cloning feature to process its own files and posting in to the site."""

import requests
import re


# TODO: give the variables better names
# TODO: does the module import inside the function affect the scripts execution time? haven't found a way yet to call them in csv_m properly, when they get imported at the start
# TODO: exception clause for mixdrop since they deactivate their upload via API from time to time due to maintenance
# TODO: maybe a general exception clause if a hoster isn't available

def mixdrop():
    import csv_m
    # mixdrop requires mail + api key
    email = "MAIL"
    old_url = (''.join(csv_m.rows[5]))
    api_mixdrop = "API KEY"
    upload_mixdrop = f'https://api.mixdrop.co/remoteupload?email={email}&key={api_mixdrop}&url={old_url}'
    request_mixdrop = requests.get(upload_mixdrop)
    response_mixdrop = request_mixdrop.json()
    filecode_mixdrop = response_mixdrop["result"]["fileref"]  # new filecode is nested along with other information
    return filecode_mixdrop


def gounlimited():
    """gounlimited only requires an api key, but has its own way to deal with file cloning.
    file code equals everything after the last slash of the video url - generate it with regex"""
    api_gounlimited = 'API KEY'
    import csv_m

    """opens csv after csv to retrieve the old existing stream-link, parses it through the GO API
            then retrieves the stream link of the new uploaded video and prints it."""

    old_url = ''.join(csv_m.rows[4])
    file_code = ''.join(re.findall('[^\/]+$', old_url))  # file code means everything after the last slash of the stream url
    upload_gounlimited = f'https://api.gounlimited.to/api/file/clone?key={api_gounlimited}&file_code={file_code}'
    request_gounlimited = requests.get(upload_gounlimited)
    go_response = request_gounlimited.json()
    go_vid_url = go_response["result"]["filecode"]
    return go_vid_url
