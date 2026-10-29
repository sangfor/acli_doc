---
sidebar_position: 1
---

# rpcinfo

### Overview

Query RPC service registrations, including program numbers, versions, transports, addresses, and service names.

### Command Parameters

Command format:

```bash
acli system rpcinfo
acli system rpcinfo [options] [arguments]
```

Supported parameters:

This command uses a closed allowlist for read-only options. Only the listed options are permitted; other options are rejected. Without arguments, it queries local RPC registrations.

Read-only option allowlist:

```text
-a -b -l -m -n -p -s -t -T -u
```

Supply addresses, hosts, program numbers, versions, and other arguments as required by the selected query.

Forbidden arguments:

```text
-d prognum versnum    Delete the specified RPC program registration from rpcbind; this is a write operation and is rejected
```

Combined short options are checked character by character. Any combination containing `d` is rejected.

`-Z` (uppercase Z) is only a probe used to extract usage information. It is outside the normal read-only option set and is not permitted.

### Usage Example

```bash
acli system rpcinfo
```

### Output Example

```text
   program version netid     address                service    owner
    100000    4    tcp6      ::.0.111               portmapper superuser
    100000    3    tcp6      ::.0.111               portmapper superuser
    100000    4    udp6      ::.0.111               portmapper superuser
    100000    3    udp6      ::.0.111               portmapper superuser
    100000    4    tcp       0.0.0.0.0.111          portmapper superuser
    100000    3    tcp       0.0.0.0.0.111          portmapper superuser
    100000    2    tcp       0.0.0.0.0.111          portmapper superuser
    100000    4    udp       0.0.0.0.0.111          portmapper superuser
    100000    3    udp       0.0.0.0.0.111          portmapper superuser
    100000    2    udp       0.0.0.0.0.111          portmapper superuser
    100000    4    local     /var/run/rpcbind.sock  portmapper superuser
    100000    3    local     /var/run/rpcbind.sock  portmapper superuser
    100024    1    udp       0.0.0.0.150.80         status     superuser
    100024    1    tcp       0.0.0.0.150.80         status     superuser
    100024    1    udp6      ::.150.80              status     superuser
    100024    1    tcp6      ::.150.80              status     superuser
    100003    3    tcp       0.0.0.0.8.1            nfs        superuser
    100005    3    tcp       0.0.0.0.150.65         mountd     superuser
    100005    1    tcp       0.0.0.0.150.66         mountd     superuser
```
