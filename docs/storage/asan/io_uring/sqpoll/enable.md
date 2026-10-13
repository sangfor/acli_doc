---
sidebar_position: 1
---

# enable

### 操作概述

开启虚拟存储卷缓存服务中io_uring的sqpoll模式

### 命令参数

```bash
-v|--volume-id=string      必要参数，存储卷id，示例：a4ef106e_vs_vol_rep2
```

### 使用示例

```bash
acli storage asan io_uring sqpoll enable -v a4ef106e_vs_vol_rep2
```

### 结果示例

```bash
sqpoll-enable   vol=a4ef106e_vs_vol_rep2  target=sqpoll      STATUS: SUCCESS

  HOST               RESULT  DETAIL
  host-002246213d6b  OK      converged, bind ok
  host-6c92bf51945a  OK      converged, bind ok
  host-a0369f9be720  OK      converged, bind ok

  volume mode: sqpoll (persisted)
  hosts: 3/3 converged
```

若卷内某台主机未通过前置检查，则开启失败并回滚，仅展示失败主机与回滚状态：

```bash
sqpoll-enable   vol=a4ef106e_vs_vol_rep2  target=sqpoll       STATUS: FAILED

  HOST               RESULT     DETAIL
  host-002246213d6b  FAILED     precheck: kernel version below 6.6
  host-6c92bf51945a  REVERTING  applied here, cron will revert

  volume mode: interrupt (unchanged, not persisted)
  hosts: 1/2 converged
```