---
sidebar_position: 1
---

# get

### 操作概述

请求mgmt-node-agent-api获取接口数据

### 命令参数

```bash
-p|--param=string         对应get请求的请求参数，如：groupPath=/management/unstrict/asv
-g|--group-id=string      mem_group子命令需要单独指定的参数，如：compute_root_group
-s|--service-id=string    service子命令需要单独指定的参数，可通过services子命令获取，如：28b4a4e4-dde6-4777-9394-fc940f643cab
-i|--interface=string     必要参数，指定需请求的服务接口别名, 可用接口别名如下：

 available_cpus：获取可用的CPU核心列表
 cpu_procs：获取指定CPU组内进程列表
 cpu_tasks：获取指定CPU组内任务列表
 cpu_groups：获取CPU组列表
 monopoly_cpus：获取独占CPU核心列表
 children_groups：获取子组列表
 cpu_group_exists：判断指定CPU组是否存在
 cpu_groups_repair：查询CPU资源组的自修复状态
 mem_memory：获取内存使用情况
 mem_hugepage：获取HugePage内存使用情况
 mem_layout：获取内存布局信息
 mem_kernel_usage：获取内核的内存使用情况
 mem_group_repair：查询内存资源组的自修复状态
 mem_allocable_group：获取可分配内存的资源组
 mem_group：获取内存资源组列表（需要--group-id）
 list_mem_groups：获取内存资源组列表
 service：获取服务信息（需要--service-id）
 services：获取服务列表
 ping：检测服务是否可用
 compute_config：获取计算资源配置
 compute_cpu：获取计算资源CPU信息
 compute_memory：获取计算资源内存信息
```

### 使用示例

```bash
acli service asv mgmt-node-agent-api get -i service --service-id ea69d188-1966-4f26-ada7-2b2511c34ef3
```

### 结果示例

```bash
Requesting: http://127.0.0.1:15001/v1/services/ea69d188-1966-4f26-ada7-2b2511c34ef3
{
    "data": {
        "uuid": "ea69d188-1966-4f26-ada7-2b2511c34ef3",
        "max_instance_count": 1024,
        "cmdline": "",
        "config_type": "static",
        "memory": {
            "min_byte": 5368709120,
            "max_byte": 5368709120,
            "avg_byte": 5368709120
        },
        "service_type": "normal_service",
        "desc": "normal services memory, exclude system service and vs, default is 5G, may be modified just like system_service",
        "name_regex": [
            "(?P<name>.*$"
        ],
        "name": "all_normal_service"
    },
    "success": 1
}
```
