'''
Program: Connected Devices Finder
File Name: discover.py
Author: Elizabeth Acevedo
Date: 06/08/2026

Example Output:
Hostname: Elizabeth-iPhone
IP: 192.168.1.22
MAC: AA:BB:CC:DD:EE:FF
Vendor: Apple

'''

from scapy.all import Ether, ARP, srp

def broadcast():

    # Scans every possible host on the local network
    target = "192.168.1.0/24"                                   # Router IP

    # Creates an ARP request asking:"Who has this IP address?" 
    arp = ARP(pdst=target)                                      # pdst = Protocol Destination

    # Creates an Ethernet broadcast frame that is sent to everyone
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")                  

    # Combines Ethernet layer and ARP layer into one packet
    packet = broadcast / arp                                    # / used to stack protocol layers

    # Sends packet and wait up to 3 secs for replies
    # srp() returns:
    #   [0] = answered requests
    result = srp(packet, timeout=3, verbose=True)[0]      

    # Processes every device that responded
    for sent, received in result:
        print(f"IP: {received.psrc} -> MAC: {received.hwsrc}")  # psrc = protocol source (ip), hwsrc = hardware source (MAC)

    

def find_dev_host():
    host = ""
    pass

def find_dev_ip():
    dev_ip = ""
    pass

def find_dev_MAC():
    dev_mac = ""
    pass

def print_dev(host):
    print("Hostname: %s", host)
    pass


def main():
    print("\n=== Devices Found ===\n")
    #print_dev()
    broadcast()

if __name__ == '__main__':
    main()