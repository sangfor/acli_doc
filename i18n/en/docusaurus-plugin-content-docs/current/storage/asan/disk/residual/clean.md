---
sidebar_position: 1
---

# clean

### Overview

Clear residual disk information

### Command Parameters
```bash
-p|--path=string    Required parameter, Block device path, Example: /dev/sdc
```

### Usage Example

```bash
acli storage asan disk residual clean -p /dev/sdc
```

### Output Example

```bash
[INFO] =====Target device: /dev/sdd=====
[INFO] Target device: /dev/sdd (Type: disk)
[INFO] Executing security status check...
[INFO] Security check passed: Device and sub-devices are currently not mounted by the system or used as Swap
[INFO] Checking and cleaning LVM structures...
[WARN] Residual LVM VG 'vg_test' detected. Attempting to deactivate and remove...
[INFO] Successfully removed VG 'vg_test' via standard path
[INFO] Checking and cleaning underlying LVM PV labels...
[WARN] Detected orphaned LVM PV remnants, executing pvremove...
[INFO] LVM PV label on /dev/sdd1 has been cleared
[INFO] Beginning analysis and cleanup of residual low-level signatures...
[INFO] Executing wipefs -a to precisely clear all known signatures...
[INFO] Signature cleared on /dev/sdd
[INFO] /dev/sdd1 signature has been cleared
[INFO] Performing physical zeroing on head and tail
[INFO] Head and tail physical zeroing completed, TARGET_DEV:/dev/sdd
[INFO] Notifying the kernel to re-read the partition table...
[INFO] Kernel partition table refreshed (original partition nodes should have disappeared)
[INFO] =====Target device: /dev/sdd cleanup complete=====

```