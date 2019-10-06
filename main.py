import os
import json

from requests_toolbelt import MultipartEncoder
import requests

import config

USERNAME = config.username
PASSWORD = config.password

def get_auth(username, password):
    '''Enter username and password and return Authorization headers.'''

    url = "https://api.clippings.io/api/login"

    payload = dict(
        password = password,
        username = username
    )

    r = requests.post(
        url,
        data=payload
    )
    if r.status_code == 200:
        j = json.loads(r.content)
        print(session.cookies.get_dict())
        return True, j['token']
    else:
        return False, None


def upload_clippings(token, file):
    '''Provide Authorization token and file to upload.'''

    url = "https://api.clippings.io/api/UserFileUploads/"

    m = MultipartEncoder(
        fields = {
            'qquuid': 'd00696d7-becf-4032-9b78-b65404488907',
            'qqfilename': file,
            'qqtotalfilesize': str(os.stat(file).st_size),
            'qqfile': ('file', open(file, "rb"), 'text/plain')
        }
    )

    r = requests.post(
        url,
        data=m,
        headers={
            'Authorization': str(token),
            'Content-Type': m.content_type
            }
    )

    #Currently it returns 200 and error 'has an invalid extension'
    print(r.status_code)
    print(r.content)

result, token = get_auth(USERNAME,PASSWORD)
upload_clippings(token, 'My Clippings.txt')
