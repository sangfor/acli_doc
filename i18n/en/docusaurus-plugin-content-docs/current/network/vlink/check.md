---
sidebar_position: 1
---

# check

### Overview

Check vlink configuration status

### Command Parameters
```bash
-s|--service=string     Required parameter, Type of check, Enumeration values: vm (VM), cluster (all VMs in the current cluster), host (all VMs on a single node), nk (northbound Kafka), sk (southbound Kafka), vt (platform), mp (management plane), ccp (central controller), redis (Redis cache), lcp (local controller), dp (data plane), Enum values: vm,cluster,host,nk,sk,vt,mp,redis,ccp,lcp,dp
-v|--vm-id=string       VM ID, Example: 4872898137715, Default: 
-h|--hostname=string    Node ID, Example: host-005056893c9d, Default: 
```

### Usage Example

```bash
acli network vlink check --service vm --vm-id 1517895970957
```

### Output Example

```bash
=== Service Query Result ===
Service     VMPort                                Location           Peer
VM          1517895970957                         host-005056b2ec8d  -
MP          8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
NorthKafka: Not detected | Not detected | Not detected
CCP         8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
SouthKafka: Not Detected | Not Detected | Not Detected
Redis       8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
LCP         8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
DP          8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c

=== Precautions ===
1. Before performing any disposal operations, collect logs using the available tools.
2. Both Kafka and CCP use incremental message logs stored by the service as their information source, rather than full configuration data. If the accurate configuration information cannot be found, the output will be "Not Detected".
3. Except for Kafka and CCP services, all other service information sources use full configuration data. If the relevant configuration cannot be found, output "Not Found".
4. Location is based on the information provided by VM; all other items are based on the configuration information provided by MP.
5. This tool cannot guarantee the consistency of service configurations across all layers during the detection process. Avoid performing network configuration updates during tool usage, as this may lead to misjudgments. You may attempt to execute the check multiple times to further confirm the issue.
```