#1st lab 2nd part

import paramiko
import time
import re

HOSTIP = '10.31.70.209'
PORT = '55443'
LOGIN = 'restapi'
PASS = 'j0sg1280-7@'
TIMEOUT = 1
BUF_SIZE = 64000

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect(HOSTIP, username=LOGIN, password=PASS, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("terminal length 0 \n")
time.sleep(TIMEOUT)

session.send("\n")
session.recv(BUF_SIZE)
session.send("show interface\n")
time.sleep(TIMEOUT*3)
s = session.recv(BUF_SIZE).decode()
session.close()


outlist=s.split('\n')
n = 0
#for i in outlist:
#    n += 1
#    print("Line" , str(n), ":", i)
intstat = dict()
intlist =[]
for line in outlist:
    m = re.search(r'^\s*Hardware is', line)
    if bool(m): continue
    m = re.search(r'^(\S+)\s+is\s+', line)
    if bool(m):
        interface = str(m.group(1))
        intstat[interface] = dict()
        intlist.append(interface)
        continue
    m = re.search(r'^\s*(\d+)\s+packets input,\s+(\d+)\s+bytes', line)
    if bool(m):
        intstat[interface]['packin']=int(m.group(1))
        intstat[interface]['bytein']=int(m.group(2))
        continue
    m = re.search(r'^\s*(\d+)\s+packets output,\s+(\d+)\s+bytes', line)
    if bool(m):
        intstat[interface]['packout']=int(m.group(1))
        intstat[interface]['byteout']=int(m.group(2))
        continue

for i in intlist:
    print("Interface:", i, end=" ")
    print("packet in/out:", intstat[i]['packin'], "/", intstat[i]['packout'],
          "; bytes in/out:", intstat[i]['bytein'], "/", intstat[i]['byteout'])


