---
sidebar_position: 1
---

# get

### Overview

Query a single virtual machine NIC type (cold-edit query, works in both powered-on and powered-off states; returns the details of a single NIC).

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID, must be numeric digits only, example: 4133790374747
-n|--nic-id=string   Required parameter, single NIC ID (UUID format, i.e. the iface_id field in the conf file), example: 34a89548-2923-4a87-93ab-ee71846fb6ba
```

### Usage Example

```bash
acli vm advcfg nic-type get --vm-id 4133790374747 --nic-id 34a89548-2923-4a87-93ab-ee71846fb6ba
```

### Output Example

```bash
nics:
  [0]:
    macAddress: FE:FC:FE:0D:5D:88
    model: e1000
    nicID: 34a89548-2923-4a87-93ab-ee71846fb6ba
    nicName: net0
```
