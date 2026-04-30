---
sidebar_position: 1
---

# sync

### Overview

Sync all installed plugins and their configuration to specified cluster nodes

### Command Parameters

```bash
-o|--host=string    Required. Target host IP list, separate multiple IPs with commas. Example: 192.168.1.10,192.168.1.11
```

### Usage Example

```bash
acli plugin sync -o 192.168.1.10

acli plugin sync -o 192.168.1.2,192.168.1.3
```

### Output Example

```bash

acli plugin sync -o 10.131.136.168
Cannot sync to the master node itself, please specify other cluster nodes.

acli plugin sync -o 10.131.136.168,10.10.10.01
Error: The following IPs are not cluster members and cannot be synced: 10.10.10.01

acli plugin sync -o 10.131.136.11,10.131.136.12
Error: The following IPs are not cluster members and cannot be synced: 10.131.136.11, 10.131.136.12

acli plugin sync -o 10.131.136.168,10.131.136.28
Plugin synchronization completed

```