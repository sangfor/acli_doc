---
sidebar_position: 1
---

# set

### Overview

Modify the custom QEMU args of the VM machine (cold edit, only supported when the VM is powered off)

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 6520699837375
-V|--value=string    Required parameter, machine custom QEMU args string (motherboard/BIOS args), example: -no-hpet -nodefaults. Overwrite semantics: a value replaces it, an empty string clears it. Note: for values starting with -, use the = form (e.g. -V="-no-hpet -nodefaults") to avoid being parsed as an option; values must not contain high-risk Linux command words (e.g. reboot), otherwise they are blocked by the security filter
```

### Usage Example

```bash
acli vm advcfg machine-args set -v 6520699837375 -V="-no-hpet -nodefaults"
```

### Output Example

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
argsAfter: -no-hpet -nodefaults
argsBefore:
vmID: 6520699837375
```

Rejected while the VM is running:

```bash
Error: the VM is running, please power it off before modifying the custom QEMU args!
```

Blocked when the value contains a high-risk command word:

```bash
Error: the input string contains the high-risk Linux command: reboot, the operation is rejected.
```