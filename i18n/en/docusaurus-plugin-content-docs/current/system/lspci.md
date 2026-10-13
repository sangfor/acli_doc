---
sidebar_position: 1
---

# lspci

### Overview

View node PCIe device information

### Command Parameters

```bash
-n  Display vendor and device IDs as digits
-v  Display detailed device information
-k  Display kernel driver corresponding to the device
-d  Filter devices by vendor/device ID
```

### Usage Example

```bash
acli system lspci -v
```

### Output Example

```bash
00:00.0 Host bridge: Intel Corporation Device 2020 (rev 06)
        Subsystem: Intel Corporation Device 2020
        Flags: bus master, fast devsel, latency 0
        Capabilities: [e0] Vendor Specific Information: Len=14 <?>

00:01.0 PCI bridge: Intel Corporation Device 2030 (rev 06)
        Flags: bus master, fast devsel, latency 0
        Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
        ...
```
