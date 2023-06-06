from gsheet import get_meeting_id

import jwt
import requests
import json
import os
from time import time
import pandas


API_KEY = os.getenv('API_KEY')
API_SEC = os.getenv('API_SEC')

meetingId = get_meeting_id()


def generateToken():
    token = jwt.encode(
        {'iss': API_KEY, 'exp': time() + 5000},
        API_SEC,
        algorithm='HS256'
    )
    return token


def getUsers():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}

    r = requests.get('https://api.zoom.us/v2/users/', headers=headers)
    print("\n fetching zoom meeting info now of the user ... \n")
    print(r.text)


def attendance():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.get(
        f'https://api.zoom.us/v2/metrics/meetings/{meetingId}/participants', headers=headers)
    data = r.json()
    df = pandas.DataFrame(data['participants'])
    print(df)
    df.to_csv('attendance.csv')


if __name__ == '__main__':
    getUsers()
    attendance()
