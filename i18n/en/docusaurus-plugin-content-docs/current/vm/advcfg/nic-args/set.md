---
sidebar_position: 1
---

# set

### Overview

Modify the custom QEMU args of the VM NIC (cold edit, only supported when the VM is powered off)

### Command Parameters

```bash
-v|--vm-id=string     Required parameter, virtual machine ID, example: 6520699837375
-t|--type=string      Required parameter, scope, enum values: vm (modify all NICs of the VM), nic (modify only the single NIC specified by --nic-id), case-insensitive, example: nic. Only supported when the VM is powered off
-n|--nic-id=string    Optional parameter, NIC ID (iface_id), example: f89a68a0-e44f-494b-9c52-7c47100cfddd. Required when --type nic; ignored when --type vm
-V|--value=string     Required parameter, custom QEMU args string (plain comma-separated), example: mq=on,vectors=8. Overwrite semantics: a value replaces it, an empty string clears it. Note: for values starting with -, use the = form; values must not contain high-risk Linux command words, otherwise they are blocked by the security filter
```

### Usage Example

```bash
# Modify a single NIC
acli vm advcfg nic-args set -v 6520699837375 -t nic -n f89a68a0-e44f-494b-9c52-7c47100cfddd -V "mq=on,vectors=8"
# Modify all NICs
acli vm advcfg nic-args set -v 6520699837375 -t vm -V "mq=on,vectors=8"
```

### Output Example

Modify a single NIC (`--type nic`):

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
nicIDs:
  [0]: f89a68a0-e44f-494b-9c52-7c47100cfddd
perNicChanges:
  [0]:
    customArgsAfter: mq=on,vectors=8
    customArgsBefore:
    index: 0
    nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
    nicName: net0
scope: nic
vmID: 6520699837375
```

Modify all NICs (`--type vm`):

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
nicIDs:
  [0]: f89a68a0-e44f-494b-9c52-7c47100cfddd
perNicChanges:
  [0]:
    customArgsAfter: mq=on,vectors=8
    customArgsBefore:
    index: 0
    nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
    nicName: net0
scope: vm
vmID: 6520699837375
```