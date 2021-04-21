#!/usr/local/bin/python

from pysnmp.hlapi import *

vers = getCmd(SnmpEngine(),
                 CommunityData('public', mpModel=0),
                 UdpTransportTarget(('10.31.70.107', 161)),
                 ContextData(),
                 ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

eth = nextCmd(SnmpEngine(),
                 CommunityData('public', mpModel=0),
                 UdpTransportTarget(('10.31.70.107', 161)),
                 ContextData(),
                 ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode=False)

for z in vers:
   for a in z[3]:
        print(a)

for y in eth:
    for a in y[3]:
        print(a)

