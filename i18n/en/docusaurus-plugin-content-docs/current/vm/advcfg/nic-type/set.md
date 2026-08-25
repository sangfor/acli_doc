---
sidebar_position: 1
---

# set

### Overview

Set virtual machine NIC type (cold edit, VM must be in powered-off state). This command changes all NICs of the VM to the target model uniformly, not a single NIC; a confirmation prompt is triggered before execution; the change takes effect at the qemu layer on the next VM power-on.

Constraints:
- VM must be powered off; powered-on state is rejected (HTTP 500).
- Only `virtio` / `e1000` models are supported, case-insensitive.
- Windows without vmtools installed is not allowed to change e1000→virtio (virtio driver depends on vmtools); the reverse direction and Linux in both directions are not restricted.

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID, must be numeric digits only, example: 4133790374747
-m|--model=string    Required parameter, target NIC model, enum value, virtio: high-performance paravirtualized NIC driver, requires vmtools to be installed in the guest; e1000: Intel 82540EM emulated NIC, best compatibility without vmtools; case-insensitive, example: virtio
```

### Usage Example

```bash
acli vm advcfg nic-type set --vm-id 4133790374747 --model virtio
```

### Output Example

```bash
Are you sure you want to perform this operation? (y[es]/n[o]): y
newModel: virtio
nics:
  [0]:
    mac: FE:FC:FE:0D:5D:88
    newModel: virtio
    nicID: 34a89548-2923-4a87-93ab-ee71846fb6ba
    nicName: net0
    oldModel: e1000
  [1]:
    mac: FE:FC:FE:D3:B0:44
    newModel: virtio
    nicID: a05805f9-7e8b-44fe-91a7-a84a3b83eb50
    nicName: net1
    oldModel: e1000
  [2]:
    mac: FE:FC:FE:5E:98:71
    newModel: virtio
    nicID: 67666518-52c0-40d9-aeb4-d0f9a5e33e35
    nicName: net3
    oldModel: e1000
  [3]:
    mac: FE:FC:FE:A3:B0:D5
    newModel: virtio
    nicID: e01943c5-fea9-4f5d-ae60-e472e1ab7491
    nicName: net2
    oldModel: e1000
oldModel: e1000
vmID: 4133790374747
```
