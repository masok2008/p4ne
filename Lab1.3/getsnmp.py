#3rd Lab file

from pysnmp.hlapi import *

address = ('10.31.70.107', 161)
getvers = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
getint = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

def result_print(snmp_gen):
    for rez in snmp_gen:
        for s in rez[3]:
            print(s)
    print(" ")



genver = getCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget(address),
               ContextData(), ObjectType(ObjectIdentity(getvers)))
genint = nextCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget(address),
               ContextData(), ObjectType(ObjectIdentity(getint)), lexicographicMode=0)
result_print(genver)
result_print(genint)

