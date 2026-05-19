---
sidebar_position: 2
---

# set

### Overview

Modify scheduler quota

### Command Parameters
```bash
--params=object                         Required parameter, Quota parameter object
--params.clusterQuota=integer           Cluster quota limit
--params.faultToleranceQuota=integer    Fault tolerance quota
--params.nodeQuota=integer              Node quota limit
--params.resourceType=string            Resource type
```

### Usage Example

```bash
acli platform scheduler quota set --params.resourceType computeOperate --params.nodeQuota 35
```

### Output Example

```bash
nodeQuota: 10
resourceType: computeOperate
```