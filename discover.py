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
import socket

def broadcast():
    ip_lst = []
    mac_lst = []

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
        ip_lst.append(received.psrc)                            # Store discovered IP addresses for hostname lookup later
        mac_lst.append(received.hwsrc)                          # Store discovered MAC addresses for device display later
                                                                 # psrc = protocol source (ip), hwsrc = hardware source (MAC)
    return ip_lst, mac_lst

'''Performs a reverse DNS lookup on each discovered 
IP address and displays the hostname, IP address, and MAC address.'''
def find_dev_host(ip_lst, mac_lst):
    dev_num = 1                             # Device counter variable for user-friendly output
    hostname = ""                           # Empty hostname
    
    # Iterates through matching IP and MAC addresses simultaneously
    for ip, mac in zip(ip_lst, mac_lst):
        
        try:
            # Attempt reverse DNS lookup:
            # Given an IP address, retrieve the associated hostname
            hostname = socket.gethostbyaddr(ip)[0]

        except socket.herror:
            # Devices that don't provide hostname information
            hostname = "Unknown"

        # Display device information
        print(f"\n\nDevice {dev_num}: ")

        print(f"\nHostname: {hostname}")
        print(f"\nIP Address: {ip}")
        print(f"\nMAC Address: {mac}")
        
        dev_num += 1                        # Move to next device number for display

def print_devs():
    print("\n=== Devices Found ===\n")

    ip_lst, mac_lst = broadcast()
    find_dev_host(ip_lst, mac_lst)

def main():
    print_devs()
    

if __name__ == '__main__':
    main()