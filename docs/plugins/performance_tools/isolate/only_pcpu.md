---
sidebar_position: 2
---

# only_pcpu

### 操作概述

指定 CPU 核心隔离

### 命令参数

```bash
-c|--cpustr=string            必要参数，需要隔离的 CPU：'1,2,3,7-9'，隔离虚拟机或指定核心时参数有效
```

### 使用示例

```bash
# 示例1：隔离指定的 CPU 核心
acli performance_tools isolate only_pcpu -c 0
```

### 结果示例

```bash
将会迁移vn管控面进程 
将会迁移根目录进程 
将会使用mgmt api进行隔离 

独占的PCPU范围是: 0 
网络转发核独占的PCPU范围是: 1 
非独占虚拟机的PCPU范围是: 2-7。 
vs管理面的PCPU范围是: 2-7。 
vs数据面客户端的PCPU范围是: 2-7。 
vs数据面服务端的PCPU范围是: 2-7。 
已经被独占的PCPU（包括only_pcpu独占和独占虚拟机）范围是: 。 
    Numa Node 0 非独占虚拟机的允许使用的PCPU范围: 2-7 

创建cgroup /isolate_vm
null
cgroup (/isolate_vm) 绑定cpu范围为：[0]
null
创建cgroup /isolate_vm/only_pcpu
null
cgroup (/isolate_vm/only_pcpu) 绑定cpu范围为：[0]
null
设置vs客户端cgroup
cgroup(/sys/fs/cgroup/cpuset/storage/svc_nfs) 绑定cpu范围为：2-7
cgroup (/storage/svc_nfs) 绑定cpu范围为：[2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_ssdc) 绑定cpu范围为：2-7
cgroup (/storage/svc_ssdc) 绑定cpu范围为：[2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_tgtd) 绑定cpu范围为：2-7
cgroup (/storage/svc_tgtd) 绑定cpu范围为：[2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_mds) 绑定cpu范围为：2-7
cgroup (/storage/svc_mds) 绑定cpu范围为：[2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_vhost) 绑定cpu范围为：2-7
cgroup (/storage/svc_vhost) 绑定cpu范围为：[2-7]
null

设置vs服务端cgroup
cgroup(/sys/fs/cgroup/cpuset/storage/svc_fsd) 绑定cpu范围为：2-7
cgroup (/storage/svc_fsd) 绑定cpu范围为：[2-7]
null
cgroup(/sys/fs/cgroup/cpuset/storage/svc_tierd) 绑定cpu范围为：2-7
cgroup (/storage/svc_tierd) 绑定cpu范围为：[2-7]
null

设置vs管理面cgroup
cgroup(/sys/fs/cgroup/cpuset/asan) 绑定cpu范围为：2-7
cgroup (/asan) 绑定cpu范围为：[2-7]
{"message":"\u00011192msg1120资源组（%(group_id)s）不存在par1121{\"group_id\": \"/asan\"}domain1115mgmt_node_agentproduct03HCI","code":"0x04000075","title":"Bad Request"}
设置cgroup(/sys/fs/cgroup/cpuset/asan/cpuset.cpus)为[2-7]失败，实际为[]！
 cgroup(/sys/fs/cgroup/cpuset/asan) 绑定cpu范围为：2-7 失败，请稍后重新运行脚本！ 

设置vt管理面cgroup
cgroup(/sys/fs/cgroup/cpuset/service) 绑定cpu范围为：2-7
cgroup (/service) 绑定cpu范围为：[2-7]
{"message":"\u00011195msg1120资源组（%(group_id)s）不存在par1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x04000075","title":"Bad Request"}
设置cgroup(/sys/fs/cgroup/cpuset/service/cpuset.cpus)为[2-7]失败，实际为[]！
 cgroup(/sys/fs/cgroup/cpuset/service) 绑定cpu范围为：2-7 失败，请稍后重新运行脚本！ 

设置vn管理面 cgroup
创建cgroup /service/vn_manager
{"message":"\u0001120101msg1126父资源组（%(group_id)s）不存在，请先创建par1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x0400005F","title":"Bad Request"}
迁移cgroup /network 的pid到 /service/vn_manager

设置根目录 cgroup
创建cgroup /service/svc_root
{"message":"\u0001120101msg1126父资源组（%(group_id)s）不存在，请先创建par1124{\"group_id\": \"/service\"}domain1115mgmt_node_agentproduct03HCI","code":"0x0400005F","title":"Bad Request"}
迁移cgroup / 的pid到 /service/svc_root

设置计算面 cgroup
cgroup(/sys/fs/cgroup/cpuset/compute) 绑定cpu范围为：2-7
cgroup (/compute) 绑定cpu范围为：[2-7]
null
cgroup(/sys/fs/cgroup/cpuset/compute/6025407369236) 绑定cpu范围为：2-7


独占结果（空表示没有）： 
独占的pcpu范围:  
0
```
