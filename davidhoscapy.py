import sys
from scapy.all import *
IP_input = raw_input("Please enter an IP Address: ")
print "You entered", IP_input

l3 = IP(dst=IP_input)/TCP()
l2 = Ether()/l3
l2.show()
