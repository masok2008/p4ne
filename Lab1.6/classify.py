# 6th Py file

import ipaddress
import re
import glob

def classify(line :str):
    m = re.search(r'^\s*ip address\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s*$', line)
    if bool(m):
        ipidr=m.group(1) + "/" + m.group(2)
#        print(ipidr)
        ip=ipaddress.IPv4Interface(ipidr)
        return {'ip': ip}
    m = re.search(r'^\s*interface\s+(\S+)\s*', line)
    if bool(m):
        return {'int': m.group(1)}
    m = re.search(r'^\s*hostname\s+(\S+)\s*', line)
    if bool(m):
        return {'host': m.group(1)}
    return {}
pathtofiles="C:\\Users\\user\\Seafile\\p4ne_training\\config_files"
netobj=dict()
netobj['ip']=[]
netobj['int']=[]
netobj['host']=[]

files=glob.glob(pathtofiles+"\\*.txt")
for fn in files:
    with open(fn) as f:
        for str in f:
            d = classify(str)
            for key, value in d.items():
                netobj[key].append(value)

netobj['ip']=list(set(netobj['ip']))
netobj['int']=list(set(netobj['int']))
netobj['host']=sorted(list(set(netobj['host'])))
print("Hosts:")
for str in netobj['host']:
    print(str, end= " ")
print("\nInterfaces:")
for str in netobj['int']:
    print(str, end= " ")
print("\nIPIDRISS:")
for str in netobj['ip']:
    print(str, end= " ")
print("\n")



