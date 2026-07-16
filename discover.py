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
# IMPORTS
from scapy.all import Ether, ARP, srp
import socket
import datetime
import network_monitor

'''Performs an ARP request asking connected devices to return their MAC address 
and collects what IP belongs to what device'''
def discover_devices():
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
    responses = srp(packet, timeout=3, verbose=True)[0]      

    # Processes every device that responded
    for sent, received in responses:
        ip_lst.append(received.psrc)                            # Store discovered IP addresses for hostname lookup later
        mac_lst.append(received.hwsrc)                          # Store discovered MAC addresses for device display later
                                                                 # psrc = protocol source (ip), hwsrc = hardware source (MAC)
    return ip_lst, mac_lst

'''Performs a reverse DNS lookup on each discovered 
IP address and displays the hostname, IP address, and MAC address.'''
def find_dev_host(ip):
    hostname = ""                           # Empty hostname
    
    try:
        # Attempt reverse DNS lookup:
        # Given an IP address, retrieve the associated hostname
        hostname = socket.gethostbyaddr(ip)[0]

    except socket.herror:
        # Devices that don't provide hostname information
        hostname = "Unknown"

    return hostname
        
'''Processes every discovered device'''
def process_devices(cursor):
    ip_lst, mac_lst = discover_devices()

    timestamp = date_time()

    dev_num = 1

    # Iterates through matching IP and MAC addresses simultaneously
    for ip, mac in zip(ip_lst, mac_lst):
        hostname = find_dev_host(ip)

        #display_devs(dev_num, hostname, ip, mac, timestamp)
        network_monitor.save_device(cursor, hostname, mac, ip, timestamp)
    
        dev_num += 1
     

'''Displays discovered devices'''
def display_devs(dev_num, hostname, ip, mac, timestamp):
    # Display device information
    print(f"\n\nDevice{dev_num}: ")
    print(f"\nHostname: {hostname}")
    print(f"\nIP Address: {ip}")
    print(f"\nMAC Address: {mac}")
    print(f"\nTime: {timestamp}")

'''Collects current time and date'''
def date_time():
    day_time = datetime.datetime.now()
    timestamp = day_time.strftime("%m-%d-%Y   %I:%M:%S %p")
    return timestamp


def main():
    connection, cursor = network_monitor.init_db()
    timestamp = date_time()
    process_devices(cursor)
    #network_monitor.clear_database(cursor)
    network_monitor.show_db(cursor, timestamp)
    network_monitor.close_db(connection)
    

if __name__ == '__main__':
    main()