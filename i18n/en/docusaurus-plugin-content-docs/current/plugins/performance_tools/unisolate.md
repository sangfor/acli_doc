---
sidebar_position: 4
---

# unisolate

### Overview

Cancel CPU isolation, restore settings; cancel virtual machine isolation

### Command Parameters

```bash
No parameters (this command does not require parameters)
```

### Usage Example

```bash
# Example 1: Cancel CPU isolation and restore settings
acli performance_tools unisolate
```

### Output Example

```bash
Network forwarding core exclusive PCPU range is: 1 
Non-exclusive VM PCPU range is: 0,2-7. 
Already exclusive PCPU (including only_pcpu exclusive and exclusive VM) range is: . 
    Numa Node 0 Non-exclusive VM allowed PCPU range: 0,2-7 

Setting vs cgroup
Executing: /sf/bin/vsmgr tools create-cpu-group --not_bind_cpu
Setting vt management plane cgroup
cgroup(/sys/fs/cgroup/cpuset/service) binding cpu range is: 0,2-7
cgroup (/service) binding cpu range is: [0,2-7]
{"message":"\u00011195msg1120resource group (%(group_id)s) does not existpar1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x04000075","title":"Bad Request"}
Setting cgroup(/sys/fs/cgroup/cpuset/service/cpuset.cpus) to [0,2-7] failed, actual is []! 
 cgroup(/sys/fs/cgroup/cpuset/service) binding cpu range to 0,2-7 failed, please retry later! 

Setting compute plane cgroup
cgroup(/sys/fs/cgroup/cpuset/compute) binding cpu range is: 0,2-7
cgroup (/compute) binding cpu range is: [0,2-7]
null

Cancel VM and pcpu exclusive (excluding VM exclusive configured via page)
Delete cgroup /isolate_vm/only_pcpu
null
Delete cgroup /isolate_vm
null
```
