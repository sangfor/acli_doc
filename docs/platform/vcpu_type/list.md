---
sidebar_position: 1
---

# list

### 操作概述

查询集群支持的和全部 vCPU 型号

### 命令参数

```bash
无参数
```

### 使用示例

```bash
acli platform vcpu_type list
```

### 结果示例

```bash
{
  "all_vcpu": [
    {
      "description": "将 Intel® “core2duo” Generation 处理器的基准功能集作为新建虚拟机默认的vCPU功能集。将允许具有以下类型处理器的主机进入集群：Intel® “Merom” Generation （Xeon® Core™2）、Intel® “Penryn” Generation （Xeon® 45nm Core™2）、Intel® “Nehalem” Generation （Xeon® Core™ i7）、Intel® “Westmere” Generation （Xeon® 32nm Core™ i7）、Intel® “Sandy Bridge” Generation、Intel® “Ivy Bridge” Generation、Intel® “Haswell” Generation、Intel® “Broadwell” Generation、Intel® “Skylake” Generation、Intel® “Cascade Lake” Generation、Intel® “Ice Lake” Generation、Intel® “Sapphire Rapids” Generation 及未来的 Intel® 处理器。",
      "vcpu": "core2duo"
    },
    {
      "description": "将 Intel® “Haswell” Generation 处理器的基准功能集作为新建虚拟机默认的vCPU功能集。将允许具有以下类型处理器的主机进入集群：Intel® “Haswell” Generation、Intel® “Broadwell” Generation、Intel® “Skylake” Generation、Intel® “Cascade Lake” Generation、Intel® “Ice Lake” Generation、Intel® “Sapphire Rapids” Generation 及未来的 Intel® 处理器。与 Intel® core2duo 模式相比，此模式可提供更多的 CPU 功能，其中包括 RDRAND、MOVBE、INVPCID、XSAVEOPT、PCLMULQDQ、ARAT 、高级矢量扩展 2、合成乘加、事务性同步扩展以及新的位操作指令。",
      "vcpu": "Haswell-noTSX"
    },
    {
      "description": "将 Intel® “Cascade Lake” Generation 处理器的基准功能集作为新建虚拟机默认的vCPU功能集。将允许具有以下类型处理器的主机进入集群：Intel® “Cascade Lake” Generation 、Intel® “Ice Lake” Generation、Intel® “Sapphire Rapids” Generation 及未来的 Intel® 处理器。与 Intel® “Haswell” Generation 模式相比，此模式可提供更多的 CPU 功能，其中包括 PDPE1GB、RDSEED、CLWB、VNNI、Transactional Synchronization Extensions、Supervisor Mode Access Prevention、Multi-Precision Add-Carry Instruction Extensions、PREFETCHW、高级矢量扩展 512、永久内存支持指令、保护密钥权限、以紧凑格式保存处理器扩展状态和保存处理器扩展状态监控和 XGETBV with ECX = 1。",
      "vcpu": "Cascadelake-Server-noTSX"
    },
    {
      "description": "将 Intel® “Ice Lake” Generation 处理器的基准功能集作为新建虚拟机默认的vCPU功能集。将允许具有以下类型处理器的主机可以进入集群：Intel® “Ice Lake” Generation、Intel® “Sapphire Rapids” Generation 及未来的 Intel® 处理器。与 Intel® “Cascade Lake” Generation 模式相比，此模式可提供更多的 CPU 功能，其中包括 SHA 扩展、Vectorized AES、User Mode Instruction Prevention、Read Processor ID、Fast Short REP MOV、WBNOINVD、Galois Field New Instructions、AVX512 Integer Fused Multiply Add、Vectorized Bit Manipulation 和 Bit Algorithms Instructions。",
      "vcpu": "Icelake-Server-v4"
    }
  ],
  "supported_vcpu": [
    "core2duo",
    "Haswell-noTSX",
    "Cascadelake-Server-noTSX"
  ],
  "vcpu_unsupported_nodes": {
    "Icelake-Server-v4": [
      {
        "nodeid": "host-0050568e74c8",
        "nodeip": "10.131.136.197",
        "nodename": "10.131.136.197"
      },
      {
        "nodeid": "host-0050568ec35e",
        "nodeip": "10.131.137.114",
        "nodename": "10.131.137.114"
      },
      {
        "nodeid": "host-0050568e3fe4",
        "nodeip": "10.131.137.124",
        "nodename": "10.131.137.124"
      }
    ]
  }
}
```
