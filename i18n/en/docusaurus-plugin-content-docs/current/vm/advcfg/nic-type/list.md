---
sidebar_position: 1
---

# list

### Overview

List virtual machine NIC types (cold-edit query, works in both powered-on and powered-off states; omitting `--nic-id` returns all NICs of the VM, passing comma-separated multiple values returns the matching set, any non-match causes the entire request to error).

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID, must be numeric digits only, example: 4133790374747
-n|--nic-id=string   Optional parameter, NIC ID (UUID format), supports comma-separated multiple values (0-n), omitting returns all NICs of the VM, example: 34a89548-2923-4a87-93ab-ee71846fb6ba,a05805f9-7e8b-44fe-91a7-a84a3b83eb50
```

### Usage Example

```bash
acli vm advcfg nic-type list --vm-id 4133790374747
acli vm advcfg nic-type list --vm-id 4133790374747 --nic-id 34a89548-2923-4a87-93ab-ee71846fb6ba,a05805f9-7e8b-44fe-91a7-a84a3b83eb50
```

### Output Example

```bash
nics:
  [0]:
    macAddress: FE:FC:FE:0D:5D:88
    model: e1000
    nicID: 34a89548-2923-4a87-93ab-ee71846fb6ba
    nicName: net0
  [1]:
    macAddress: FE:FC:FE:D3:B0:44
    model: e1000
    nicID: a05805f9-7e8b-44fe-91a7-a84a3b83eb50
    nicName: net1
  [2]:
    macAddress: FE:FC:FE:5E:98:71
    model: e1000
    nicID: 67666518-52c0-40d9-aeb4-d0f9a5e33e35
    nicName: net3
  [3]:
    macAddress: FE:FC:FE:A3:B0:D5
    model: e1000
    nicID: e01943c5-fea9-4f5d-ae60-e472e1ab7491
    nicName: net2
```
