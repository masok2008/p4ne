#The Last lab of The 2nd Part

from flask import Flask, jsonify, render_template
import json
import requests
import re
import pprint

tokenurl = "https://sandboxapic.cisco.com/api/v1/ticket"
topourl = "https://sandboxapicem.cisco.com/api/v1/topology/physical-topology"
def gettopo():
    body = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    r = requests.post(tokenurl, data=json.dumps(body), headers=header, verify=False)
    ticket=r.json()['response']['serviceTicket']
#pprint.pprint(r.json())
#print(ticket)

    header = {"content-type": "application/json", "X-Auth-Token":ticket}
    r = requests.get(topourl, headers=header, verify=False)

#    pprint.pprint(r.json())
    topo = r.json()['response']
    return topo


site = Flask(__name__)
@site.route('/')
@site.route('/index')
def index():
    return render_template("topology.html")

@site.route('/api/topology')
def printtopo():
    return jsonify(topo)

if __name__ == '__main__':
    topo = gettopo()
    site.run(debug=True)
