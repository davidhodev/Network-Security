import sys
from scapy.all import *
IP_input = raw_input("Please enter an IP Address: ")
print "You entered", IP_input

l3 = IP(dst=IP_input)/TCP()
l2 = Ether()/l3
l2.show()


#Question 1
myListOfIP = IP("10.20.111.2")
myListOfIP.pop()
myListOfIP.pop(0)
[i for i in myListOfIP]
destPort=TCP(dport=[80,443])
[i for i in myListOfIP/destPort]

# Question 2
p = sr(IP(dst="10.20.111.2")/ICMP())


#Question 3
sr(IP(dst="10.20.111.2", ttl=(4,25),id=RandShort())/TCP(flags=0x2))


#Question 4
#I don't know how to set the target IP as the Windows XP Machine
target_ip = "10.20.111.2"
target_port = "139"
print "Syn Flood Started"
send(IP(dst="target_ip")/TCP(dport=target_port), count=2000)
