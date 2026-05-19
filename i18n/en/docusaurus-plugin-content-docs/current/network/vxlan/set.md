---
sidebar_position: 1
---

# set

### Overview

Update cluster VXLAN configuration

### Command Parameters
```bash
-i|--id=string                         Required parameter, Cluster VXLAN resource ID, Example: 8a5987e4-ff3e-47d0-8fd1-b36d2d566439
-v|--vxlan-cluster=object              Required parameter, Update cluster VXLAN configuration
--vxlan-cluster.jumbo_frame=integer    Whether to enable jumbo frames, 0: Disable, 1: Enable
```

### Usage Example

```bash
acli network vxlan set --id 8a5987e4-ff3e-47d0-8fd1-b36d2d566439 --vxlan-cluster.jumbo_frame 0
```

### Output Example

```bash
vxlan_cluster:
  id: 8a5987e4-ff3e-47d0-8fd1-b36d2d566439
  jumbo_frame: 0
  port: 8472
  probe_enable: 1
  probe_interval_s: 30
  probe_latency_us: 10000
  probe_timeout_ms: 3000
```