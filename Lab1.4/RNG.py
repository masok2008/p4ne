# 4th python lab

import random
import ipaddress

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), False)
    def regular(self):
        return self.is_global
    def key_value(self):
        return int(self.prefixlen)*2**32+int(self.network_address)
    def key_values(self):
        return (self.netmask, self.network_address)

def netsort1(n):
    return n.key_values()

def netsort(n):
    return (n.netmask, n.network_address)
def gennet(num):
    setnet =set()
    while len(setnet) < num :
        n1=IPv4RandomNetwork()
        if n1.regular():
            setnet.add(n1)
    return list(setnet)

nn = 50
#n1=IPv4RandomNetwork()
listnet = gennet(nn)
#for s in listnet: print(s, end=" ")
#print(" ")
#listnet.sort(key=netsort1)

#for s in listnet: print(s, end=" ")
#for s in sorted(listnet): print(s)
for s in sorted(listnet, key=lambda x: x.key_values()): print(s)
