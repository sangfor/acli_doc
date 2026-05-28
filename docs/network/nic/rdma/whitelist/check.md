---
sidebar_position: 1
---

# check

### 操作概述

检查rdma白名单配置

### 命令参数

```bash
-t|--type=string                    必要参数，配置类型，vs(存储私网) 或 external_storage(外置存储)
-m|--multi-node=boolean             从所有节点收集信息，可选值: true/false，默认true
-T|--table=boolean                  以表格形式展示结果，可选值: true/false，默认true
```

### 使用示例

```bash
acli network nic rdma whitelist check -t vs
```

### 结果示例

```bash
desc                                                    | vendor_id | device_id | ip_list                   | compatible
--------------------------------------------------------+-----------+-----------+---------------------------+-----------
VMware VMXNET3 Ethernet Controller [15ad:07b0] (rev 01) | 0x15ad    | 0x07b0    | 10.131.136.7,10.131.136.8 | false
```
