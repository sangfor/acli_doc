---
sidebar_position: 2
---

# only_pcpu

### Overview

Specify CPU core isolation

### Command Parameters

```bash
-c|--cpustr=string            Required parameter, CPUs to isolate: '1,2,3,7-9', parameter is valid when isolating VM or specifying cores
```

### Usage Example

```bash
# Example 1: Isolate specified CPU cores
acli performance_tools isolate only_pcpu -c 0
```

### Output Example

```bash
Will migrate vn management plane processes 
Will migrate root directory processes 
Will use mgmt api for isolation 

Exclusive PCPU range is: 0 
Network forwarding core exclusive PCPU range is: 1 
Non-exclusive VM PCPU range is: 2-7. 
VS management plane PCPU range is: 2-7. 
VS data plane client PCPU range is: 2-7. 
VS data plane server PCPU range is: 2-7. 
Already exclusive PCPU (including only_pcpu exclusive and exclusive VM) range is: . 
    Numa Node 0 Non-exclusive VM allowed PCPU range: 2-7 

Creating cgroup /isolate_vm
null
cgroup (/isolate_vm) binding cpu range is: [0]
null
Creating cgroup /isolate_vm/only_pcpu
null
cgroup (/isolate_vm/only_pcpu) binding cpu range is: [0]
null
Setting vs client cgroup
cgroup(/sys/fs/cgroup/cpuset/storage/svc_nfs) binding cpu range is: 2-7
cgroup (/storage/svc_nfs) binding cpu range is: [2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_ssdc) binding cpu range is: 2-7
cgroup (/storage/svc_ssdc) binding cpu range is: [2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_tgtd) binding cpu range is: 2-7
cgroup (/storage/svc_tgtd) binding cpu range is: [2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_mds) binding cpu range is: 2-7
cgroup (/storage/svc_mds) binding cpu range is: [2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_vhost) binding cpu range is: 2-7
cgroup (/storage/svc_vhost) binding cpu range is: [2-7]
null

Setting vs server cgroup
cgroup(/sys/fs/cgroup/cpuset/storage/svc_fsd) binding cpu range is: 2-7
cgroup (/storage/svc_fsd) binding cpu range is: [2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_tierd) binding cpu range is: 2-7
cgroup (/storage/svc_tierd) binding cpu range is: [2-7]
null

Setting vs management plane cgroup
cgroup(/sys/fs/cgroup/cpuset/asan) binding cpu range is: 2-7
cgroup (/asan) binding cpu range is: [2-7]
{"message":"\u00011192msg1120resource group (%(group_id)s) does not existpar1121{\"group_id\": \"/asan\"}domain1115mgmt_node_agentproduct03HCI","code":"0x04000075","title":"Bad Request"}
Setting cgroup(/sys/fs/cgroup/cpuset/asan/cpuset.cpus) to [2-7] failed, actual is []! 
 cgroup(/sys/fs/cgroup/cpuset/asan) binding cpu range to 2-7 failed, please retry later! 

Setting vt management plane cgroup
cgroup(/sys/fs/cgroup/cpuset/service) binding cpu range is: 2-7
cgroup (/service) binding cpu range is: [2-7]
{"message":"\u00011195msg1120resource group (%(group_id)s) does not existpar1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x04000075","title":"Bad Request"}
Setting cgroup(/sys/fs/cgroup/cpuset/service/cpuset.cpus) to [2-7] failed, actual is []! 
 cgroup(/sys/fs/cgroup/cpuset/service) binding cpu range to 2-7 failed, please retry later! 

Setting vn management plane cgroup
Creating cgroup /service/vn_manager
{"message":"\u0001120101msg1126parent resource group (%(group_id)s) does not exist, please create firstpar1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x0400005F","title":"Bad Request"}
Migrating cgroup /network pid to /service/vn_manager

Setting root directory cgroup
Creating cgroup /service/svc_root
{"message":"\u0001120101msg1126parent resource group (%(group_id)s) does not exist, please create firstpar1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x0400005F","title":"Bad Request"}
Migrating cgroup / pid to /service/svc_root

Setting compute plane cgroup
cgroup(/sys/fs/cgroup/cpuset/compute) binding cpu range is: 2-7
cgroup (/compute) binding cpu range is: [2-7]
null
cgroup(/sys/fs/cgroup/cpuset/compute/6025407369236) binding cpu range is: 2-7


Exclusive result (empty means none): 
Exclusive pcpu range:  
0
```
