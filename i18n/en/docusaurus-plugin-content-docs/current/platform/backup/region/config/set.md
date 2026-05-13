---
sidebar_position: 1
---

# set

### Overview

Set runtime parameter configuration for region snapshots

### Command Parameters
```bash
-v|--vm-id=string            Required parameter, Specifies the VM ID to identify the VM to be configured, required parameter, for example: 7441066936147
-i|--iolog=integer           Whether to print logs for each I/O related to region snapshots, Enumeration values: 0 (do not print), 1 (print), optional parameter, default value is 0, Enum values: 0,1, Default: 0
-p|--holeperf=integer        When exporting valid data areas of region snapshots, whether to skip holes, Enumeration values: 0 (do not skip holes), 1 (skip holes), optional parameter, default value is 1, Enum values: 0,1, Default: 1
-c|--cowperf=integer         Whether to enable COW high performance mode when reading region snapshots for backup, Enumeration values: 0 (disable), 1 (enable with direct method), 2 (enable with cache limit method), optional parameter, default value is 2, Enum values: 0,1,2, Default: 2
-s|--cowcachesize=integer    When cowperf is 2 (enable with cache limit method), use cowcachesize to specify the COW cache limit for the entire virtual machine, unit is MB, Valid range: 32-1024, optional parameter, default value is 256, Default: 256
-m|--cowmerge=integer        Region snapshot COW merge block count, each block corresponds to 16K, Valid range: 1-64, optional parameter, default value is 64, Default: 64
-r|--ioretry=integer         Region snapshot COW write retry count, Valid range: 0-128, optional parameter, default value is 3, Default: 3
-R|--readspeed=integer       Bandwidth limit for reading VM region snapshots, unit is KB/S, Valid range: 1-3072000, optional parameter, default value is 81920, Default: 81920
-l|--l2cachesize=integer     L2 metadata cache limit for each region snapshot image, unit is MB, Valid range: 32-1024, optional parameter, default value is 256, Default: 256
```

### Usage Example

```bash
acli platform backup region config set --vm-id=7188533957477 -i 0 --holeperf=1
```

### Output Example

```bash
This command produces no output. Upon successful modification, output is written to /sf/log/today/sfvt_qemu_{vmid}.log.
```