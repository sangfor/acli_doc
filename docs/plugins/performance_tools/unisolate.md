---
sidebar_position: 4
---

# unisolate

### 操作概述

取消 CPU 隔离，还原设置；取消虚拟机隔离

### 命令参数

```bash
无（该命令不需要参数）
```

### 使用示例

```bash
# 示例1：取消 CPU 隔离，还原设置
acli performance_tools unisolate
```

### 结果示例

```bash
网络转发核独占的PCPU范围是: 1 
非独占虚拟机的PCPU范围是: 0,2-7。 
已经被独占的PCPU（包括only_pcpu独占和独占虚拟机）范围是: 。 
    Numa Node 0 非独占虚拟机的允许使用的PCPU范围: 0,2-7 

设置vs cgroup
执行：/sf/bin/vsmgr tools create-cpu-group --not_bind_cpu
设置vt管理面cgroup
cgroup(/sys/fs/cgroup/cpuset/service) 绑定cpu范围为：0,2-7
cgroup (/service) 绑定cpu范围为：[0,2-7]
{"message":"\u00011195msg1120资源组（%(group_id)s）不存在par1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x04000075","title":"Bad Request"}
设置cgroup(/sys/fs/cgroup/cpuset/service/cpuset.cpus)为[0,2-7]失败，实际为[]！
 cgroup(/sys/fs/cgroup/cpuset/service) 绑定cpu范围为：0,2-7 失败，请稍后重新运行脚本！ 

设置计算面cgroup
cgroup(/sys/fs/cgroup/cpuset/compute) 绑定cpu范围为：0,2-7
cgroup (/compute) 绑定cpu范围为：[0,2-7]
null

解除虚拟机和pcpu独占（不包括页面配置的虚拟机独占）
删除cgroup /isolate_vm/only_pcpu
null
删除cgroup /isolate_vm
null
```
