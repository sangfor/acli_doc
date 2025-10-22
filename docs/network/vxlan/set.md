---
sidebar_position: 10
---

# set
操作概述: 开启/关闭vxlan巨帧

命令参数:
```bash
-i|--id=string 集群VXLAN资源id，示例：8a5987e4-ff3e-47d0-8fd1-b36d2d566439
-v|--vxlan-cluster.jumbo_frame=integer 是否开启巨帧：枚举值：0（关闭），1（开启）
```

使用示例:
```bash
acli network vxlan set --id 8a5987e4-ff3e-47d0-8fd1-b36d2d566439 --vxlan-cluster.jumbo_frame 0
```

结果示例:
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
