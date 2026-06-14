# Local Network Security Monitor

A Python-based network monitoring tool that discovers devices connected to a local network and collects identifying information such as IP addresses, MAC addresses, and hostnames. This project is being developed as a hands-on cybersecurity and networking project focused on network visibility, device discovery, and security monitoring.

## Features

### Current Features

* Discovers devices on the local network using ARP scanning
* Displays:
    * Hostname (when available)
    * IP Address
    * MAC Address
* Identifies devices that do not expose hostnames
* Supports scanning an entire subnet (e.g., 192.168.1.0/24)


## Example Output

=== Devices Found ===

Device 1:

Hostname: chromecast.lan
IP Address: 192.168.1.10
MAC Address: AA:BB:CC:DD:EE:FF

Device 2:

Hostname: iPhone.lan
IP Address: 192.168.1.15
MAC Address: 11:22:33:44:55:66

Device 3:

Hostname: Unknown
IP Address: 192.168.1.20
MAC Address: 77:88:99:AA:BB:CC


## How It Works

1. An ARP request is broadcast across the local network.
2. Devices respond with their IP and MAC addresses.
3. Reverse DNS lookups are performed to retrieve hostnames when available.
4. Device information is displayed to the user.


## Technologies Used

* Python
* Scapy
* Socket Library
* ARP Protocol
* Reverse DNS Lookups


### Installation

Clone the repository:
https://github.com/ElizabethAce/Local-Network-Security-Monitor.git

### Install dependencies:
python3 -m pip install scapy

### Run:
python3 discover.py


## Disclaimer

This tool is intended only for monitoring networks that you own or have explicit permission to analyze. Unauthorized network monitoring may violate laws, policies, or terms of service.


## Author: Elizabeth Acevedo
