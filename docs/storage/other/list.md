---
sidebar_position: 10
---

# list
操作概述: 获取存储分组列表

命令参数:
```bash
-v|--vsnfs=integer         (可选)如果设置为1，展示 VS NFS 存储，默认：1。枚举值：0, 1
-L|--lt256g-not-display    (可选)如果设置为1，不显示小于256G的硬盘，默认：1。枚举值：0, 1
-q|--query=string          (可选)存储名称的模式，用于过滤存储。（模糊匹配，不区分大小写）
-s|--start=integer         (可选)存储列表分页的起始索引，配合--limit一起使用。示例：--start 0 --limit 10，返回从0开始的10个
-l|--limit=integer         (可选)最大的存储返回数量，配合--start一起使用，默认从--start开始取剩下所有存储。示例：--start 0 --limit 10，返回从0开始的10个
-t|--lv-type=string        (可选)逻辑卷类型，枚举值：local, iscsi, fc, nfs, s3。默认不填，显示所有类型。
```

使用示例:
```bash
# 筛选存储，仅返回前10个类型为本地存储的存储信息
acli storage other list -v 1 -L 1 -s 0 -l 10 -t local
```

结果示例:
```bash
s3:
iscsi:
fc:
nfs:
virtual_storage:
local:
  active_host: host-0050568949a9
  maxwrite: 330139136
  used_ratio: 15.58
  urgent: 0
  total: 317827579904
  id: 36000c29922b9c9311483578fab141e6c_0050568949a9
  write_cnt: 43
  host_cnt: 1/1
  avail: 268298092544
  read_cnt: 1
  shared: 0
  nodes: host-0050568949a9
  type: local
  running_vms: 1
  status: 1
  read_ratio: 512
  used: 49529487360
  alert: 0
  disable: 0
  active: 1
  name: lv_1749527550
  maxread: 347384320
  active_host_name: 10.131.139.53
  hosts: 1
  ats: -1
  discard: 0
  write_ratio: 1076736

  active_host: host-005056893b01
  maxwrite: 406502912
  used_ratio: 0.10
  urgent: 0
  total: 317827579904
  id: 36000c293cadee3074f68ee64716b4163_005056893b01
  write_cnt: 0
  host_cnt: 1/1
  avail: 317521395712
  read_cnt: 0
  shared: 0
  nodes: host-005056893b01
  type: local
  running_vms: 0
  status: 1
  read_ratio: 0
  used: 306184192
  alert: 0
  disable: 0
  active: 1
  name: lv_1749527551
  maxread: 175596544
  active_host_name: 10.131.139.51
  hosts: 1
  ats: -1
  discard: 0
  write_ratio: 0
nof:
```