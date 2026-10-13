---
sidebar_position: 1
---

# route

### Overview

View the system routing table (read-only).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).

```bash
-n|--numeric=flag    Optional parameter. Display routes in numeric address format (do not resolve hostnames).
-e|--extend=flag     Optional parameter. Display routes in detail.
-ee                  Optional parameter. Display routes in detail (the extended form of -e).
(no parameters)      Optional parameter. Query the default routing table.
-A|--family=string   Optional parameter. Query the specified address family (inet/ipv6, etc.). Example: -A inet
-C|--cache=flag      Optional parameter. Query the routing cache.
```

Write parameters (rejected on match):

```bash
add                      Add a route (write)
del                      Delete a route (write)
flush                    Flush the routing cache (write)
-i <dev> add/del         Add/delete a route on the specified interface (write)
-host/-net with add/del  Add/delete a route for a host/network (write)
```

### Usage Example

```bash
acli system route -n
```

### Output Example

```bash
# acli system route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.0.1        0.0.0.0         UG    0      0        0 eth0
10.0.0.0        0.0.0.0         255.255.255.0   U     100    0        0 eth0
```