---
sidebar_position: 1
---

# check

### Overview

Check NIC consistency, compare MAC address and interface ID across Qemu, VN, CFS, and DB

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID. Example: 614182240912
```

### Usage Example

```bash
# Check NIC consistency
acli vm nic consistency check -v 614182240912
```

### Output Example

```bash
{"VMID":"614182240912","NICs":[{"NICIndex":0,"QemuMAC":"FE:FC:FE:DB:A3:2C","VnMAC":"FE:FC:FE:DB:A3:4C","CfsMAC":"FE:FC:FE:DB:A3:4C","CfsInterfaceID":"800b6b64-0b5d-4552-8372-b27ee991f746","VnInterfaceID":"800b6b64-0b5d-4552-8372-b27ee991f746","DBInterfaceID":"800b6b64-0b5d-4552-8372-b27ee991f746","MacConsistent":false,"IDConsistent":true,"Status":"inconsistent"}],"CheckTime":"2026-05-26T11:17:02+08:00"}
```