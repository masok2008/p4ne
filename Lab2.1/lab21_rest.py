#1st lab 2nd part

import json
import requests
import time
import re
import pprint

HOSTIP = '10.31.70.210'
PORT = '55443'
LOGIN = 'restapi'
PASS = 'j0sg1280-7@'
TIMEOUT = 1
BUF_SIZE = 64000

URL = "https://" + HOSTIP + ":" + PORT

#get token
req = URL+'/api/v1/auth/token-services'
token = requests.post(req , auth=(LOGIN, PASS), verify=False)
curr_token=token.json()['token-id']

header = {"content-type": "application/json", "X-Auth-Token": curr_token}
req = URL + '/api/v1/interfaces'
r = requests.get(req, headers=header, verify=False)
pprint.pprint(r.json())
iface=r.json()
#print(type(iface))
ifacelist = []
for i in iface['items']:
    ifacelist.append(i['if-name'])
#print(ifacelist)
ifstat = dict()
for i in ifacelist:
    ifstat[i] = dict()
    req = URL + '/api/v1/interfaces/' + i + '/statistics'
    r = requests.get(req, headers=header, verify=False)
    ifstat[i]['packin'] = r.json()['in-total-packets']
    ifstat[i]['packout'] = r.json()['out-total-packets']

pprint.pprint(ifstat)