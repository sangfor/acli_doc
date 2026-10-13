---
sidebar_position: 1
---

# arp

### Overview

View the ARP table (Address Resolution Protocol cache, read-only).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).

```bash
-n|--numeric=flag  Optional parameter. Display the ARP table in numeric address format (do not resolve hostnames). Example: acli system arp -n
```

Write parameters (rejected on match):

```bash
-s|--set <ip> <mac>  Adds an ARP entry (write)
-d|--delete <ip>     Deletes an ARP entry (write)
-f|--file <file>     Loads ARP entries from a file (write)
```

### Usage Example

```bash
acli system arp -n
```

### Output Example

```bash
# acli system arp -n
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.0.1                 ether   aa:bb:cc:dd:ee:ff   C                     eth0
10.0.0.2                 ether   11:22:33:44:55:66   C                     eth1
```
