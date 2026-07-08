## Version 0.2.5 - Initial testing of saving discovered devices into a database
- Cleaned up code in discover.py and restructured functions
- discover.py now works alongside network_monitor
- Database has been generated after first run
- Issue to be solved: Database ouput doesn't show, check show_db()

## Version 0.2.4 - Discover Devices (Now with Timestamp)
- Created network_monitor.py
- Created first draft of what will create a database - unfinished
- Added timestamp feature when discovering devices on network

## Version 0.2.3 - Code clean-up
- Commented code in discovery.py
- Created function specific to printing output on terminal

## Version 0.2.2 - Updated README
- Updated README

## Version 0.2.1 - Updated Device Display
- MAC addresses are printed under each device displayed
- Updated README
- Used zip() function (which pairs up the first items together, then the second items together, and so on) to display ip and MAC addresses

## Version 0.2.0 - Devices connected to local network, now list their hostname
- Hostnames are printed for each device aling with their ip address
- A different method may be used to achieve higher success in hostname collection.

## Version 0.1.0 - ARP Broadcast for devices connected to local network
- created discover.py
- test_discover.py (may be used for scripting later)
- First version accomplisments:
    - ARP broadcast to know what and how many devices are connected to the local network at the moment of running the program
    - Prints hosts' ip  and MAC address