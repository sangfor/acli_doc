---
sidebar_position: 1
---

# vs_update_nfs

### Overview

vs_update_nfs.sh command

### Command Parameters

No parameters

### Usage Example

```bash
acli storage asan vs_update_nfs
```

### Output Example

```bash
# acli storage asan vs_update_nfs -h
====Hot Upgrade Start Marker====
File created successfully, nfs_pid_old = 126805, nfs_supervise_pid_old = 126804
Old Process Hot Upgrade Flag Activated
Try setting user.nfs.switch with the new command:
 /sf/vs/bin/vs_rpc_tool -c set_option --pid 126805 -k user.nfs.switch -v old 2>&1
Successfully configured user.nfs.switch
Command executed successfully
Result: OK
Start a new NFS process
start new nfs: -h
 start new nfs:  failed
stop new nfs: -h
Clear Residual Markers
rm /tmp/vs/hotpath_running_flag_nfs
```