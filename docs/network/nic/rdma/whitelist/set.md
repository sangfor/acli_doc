---
sidebar_position: 1
---

# set

### 操作概述

更新rdma白名单配置

### 命令参数

```bash
-d|--device-id=string               必要参数，设备ID，用于标识具体的网卡型号，示例：0x1017
-v|--vendor-id=string               必要参数，厂商ID，用于标识网卡制造商，示例：0x15b3
-i|--ip-list=string                 待更新节点ip列表，示例：10.103.17.10,10.113.18.11
-t|--type=string                    必要参数，配置类型，vs(存储私网) 或 external_storage(外置存储)
-T|--table=boolean                  以表格形式展示结果，可选值: true/false，默认true

```

### 使用示例

```bash
acli network nic rdma whitelist set -d 0x07b0 -v 0x15ad -i 10.131.136.7,10.131.136.8 -t vs
```

### 结果示例

```bash
IP           | CPU Arch | Associated Interfaces         | Success
-------------+----------+-------------------------------+--------
10.131.136.7 | x86_64   | eth0,eth1,eth2,eth3,eth4,eth5 | true
10.131.136.8 | x86_64   | eth0,eth1,eth2,eth3,eth4,eth5 | true
```
