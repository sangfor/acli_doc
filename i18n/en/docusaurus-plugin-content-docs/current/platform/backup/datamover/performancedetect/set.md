---
sidebar_position: 1
---

# set

### Overview

Enable or disable datamover performance bottleneck detection

### Command Parameters
```bash
-v|--vm-id=string      Required parameter, Specifies the VM corresponding to the datamover, example: 7441066936147
-i|--host-id=string    Required parameter, Used to indicate the host node where the datamover service runs, example: host-9cc2c4105d08
-l|--level=string      Required parameter, Used to enable or disable datamover performance bottleneck detection, Enumeration values: 'OFF'(disable detection), 'FULL'(enable detection in full mode), 'FAST'(enable detection in fast mode), Enum values: OFF,FULL,FAST
```

### Usage Example

```bash
acli platform backup datamover performancedetect set --vm-id=7188533957477 -i=host-9cc2c4105d08 -l=FULL
```

### Output Example

```bash
Correct example:
OK
Error Case:
Error: Request failed: Unable to locate the configuration file path for the datamover process
```