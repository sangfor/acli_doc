---
sidebar_position: 1
---

# get

### Overview

Execute the read-only show query commands of SDN cli inside the vn-agent container.

### Command Parameters

```bash
<show-subcommand>  Required parameter, a read-only subcommand supported by SDN CLI. Use --list parameter to get all subcommands.
--list=flag        List all subcommands supported by SDN CLI.
```

### Usage Example

```bash
acli network cli get arp
```

```bash
acli network cli get --list
```

### Output Example

```bash
# acli network cli get arp
ARP entries:
IP               MAC                VLAN  Interface
10.10.1.2        00:0c:29:56:b7:a6  1     eth0
10.10.1.3        00:0c:29:56:aa:bb  1     eth0
```
