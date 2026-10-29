---
sidebar_position: 1
---

# vs_sn

### Overview

Query VS serial numbers and machine identifiers, and verify serial number integrity, license limits, and fusion-machine signatures.

### Command Parameters

Command format:

```bash
acli storage asan vs_sn <option>
```

The following option descriptions are from the tool's help:

```text
-f             Verify the Sangfor fusion-machine signature
-s [sn keyid]  Verify integrity and license limits of all VS serial numbers; optionally specify sn and keyid
-i             Verify integrity of all VS serial numbers
-u             Verify integrity of VS serial numbers in the local ukey
-l             Print all VS serial number information
-p             Print the VS machine identifier
-g             Print the module name from a serial number and keyid
-c             Check integrity only
-h             Print help information
```

The tool's Usage line omits `-u`, while Details includes it. The original help output is preserved below.

### Usage Example

```bash
acli storage asan vs_sn
```

### Output Example

Running `acli storage asan vs_sn` returns the following usage:

```text
Usage: vs_sn -p|-f|-s|-i|-l|-g|-c|-h
Details:
        -f       verify signature of sangfor fusion-machine
        -s [sn keyid]    verify all vs serial number integrity and authority limit
        -i       verify all vs serial number integrity
        -u       verify local ukey vs serial number integrity
        -l       print all vs serial number info
        -p       print the vs machine id
        -g       print module name from serial number and keyid
        -c       only check integrity
        -h       print help message
```
