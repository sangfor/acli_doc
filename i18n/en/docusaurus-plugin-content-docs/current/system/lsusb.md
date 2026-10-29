---
sidebar_position: 1
---

# lsusb

### Overview

List USB devices

### Command Parameters

Command format:

```bash
acli system lsusb [options]...
```

```bash
-v|--verbose=flag  Show detailed device information
-s=string          Filter by bus/device number (decimal, format: [[bus]:][devnum])
-d=string          Filter by vendor/product ID (hexadecimal, format: vendor:[product])
-D=string          Specify the USB device file to examine
-t|--tree=flag     Display devices as a tree
-V|--version=flag  Show version information
-h|--help=flag     Show help information
```

### Usage Example

```bash
acli system lsusb -h
```

### Output Example

```bash
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
```

Running `acli system lsusb -h` returns the following help:

```text
Usage: lsusb [options]...
List USB devices
  -v, --verbose
      Increase verbosity (show descriptors)
  -s [[bus]:][devnum]
      Show only devices with specified device and/or
      bus numbers (in decimal)
  -d vendor:[product]
      Show only devices with the specified vendor and
      product ID numbers (in hexadecimal)
  -D device
      Selects which device lsusb will examine
  -t, --tree
      Dump the physical USB device hierarchy as a tree
  -V, --version
      Show version of program
  -h, --help
      Show usage and help
```
