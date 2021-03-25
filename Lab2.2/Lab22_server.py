#2тв lab 2nd part

from flask import Flask
import json
import requests
import time
import re
import pprint
import ipaddress
import glob

site = Flask(__name__)

def classify(line: str):
    m = re.search(r'^\s*ip address\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s*$', line)
    if bool(m):
        ipidr = m.group(1) + "/" + m.group(2)
        ip = ipaddress.IPv4Interface(ipidr)
        return {'ip': ip}
    m = re.search(r'^\s*interface\s+(\S+)\s*', line)
    if bool(m):
        return {'int': m.group(1)}
    m = re.search(r'^\s*hostname\s+(\S+)\s*', line)
    if bool(m):
        return {'host': m.group(1)}
    return {}


def readconfig():
    pathtofiles = "C:\\Users\\user\\Seafile\\p4ne_training\\config_files"
    hostip = dict()
    files = glob.glob(pathtofiles + "\\*.txt")
    for fn in files:
        curr_host = "LOST"
        with open(fn) as f:
            for st in f:
                d = classify(st)
                for key, value in d.items():
                    if key == 'host':
                        curr_host=value
                        hostip[curr_host]=[]
                    elif key == 'ip':
                        hostip[curr_host].append(value)
    return hostip




@site.route('/')
@site.route('/index')
def index():
    st = ' / - this page<br>'
    st += ' <a href="/configs"> /configs </a> - list of device hostnames<br>'
    st += ' /config/{hostname} - list of ipaddresses of {hostname}'
    return st
@site.route('/configs')
def printdev():
    listname = sorted(list(hostip.keys()))
    sr =""
    for i in listname:
        sr += "<br><a href=\"/config/" + i + "\">" + i + "</a><br>"
    return sr
@site.route('/config/<hostname>')
def printips(hostname):
    sr = ""
    if hostname in hostip:
        sr += "<h2>" + hostname +"</h2> IP addresses: <p>"
        for i in hostip[hostname]:
            sr += "<li> " + str(i) + "<br>"
    else:
        sr = " <h3> There is not device "
    sr += """ <p><button onclick="goBack()">Go Back</button>
                <script>
                function goBack() { window.history.back();}</script> 
             """

    return sr

if __name__ == '__main__':
    hostip = readconfig()
    site.run(debug=True)

