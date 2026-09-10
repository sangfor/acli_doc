---
sidebar_position: 1
---

# mcelog

### Overview

Query CPU Machine Check Exception hardware error logs

### Command Parameters

```bash
No parameters
```

### Usage Example

```bash
acli system mcelog
```

### Output Example

```bash
HARDWARE ERROR. This is *NOT* a software problem!
Please contact your hardware vendor
CPU 0 BANK 5
MISC 4000000086
STATUS b200000000070f0f
ADDR 7f123400
MCG STATUS 0
MCG CAP 100c16
APICID 0 SOCKETID 0
CPUID Vendor GenuineIntel Family 6 Model 85
  cache or interface corrected error
  correctable error ( processor core corrected )
  FRU: memory controller, channel 0x0, DIMM 0x0
```
