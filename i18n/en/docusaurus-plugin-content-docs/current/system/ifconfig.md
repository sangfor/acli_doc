---
sidebar_position: 1
---

# ifconfig

### Overview

View node NIC configuration information

### Command Parameters

```bash
-a|--all=flag  View all NIC configuration information
<iface>        Specify NIC name to view, for example: eth0
```

### Usage Example

```bash
acli system ifconfig eth0
```

```bash
acli system ifconfig -a
```

### Output Example

```bash
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.131.136.168  netmask 255.255.255.0  broadcast 10.131.136.255
        inet6 fe80::20c:29ff:fe56:b7a6  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:56:b7:a6  txqueuelen 1000  (Ethernet)
        RX packets 520898  bytes 54239098 (51.7 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 10244  bytes 1033457 (1008.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
