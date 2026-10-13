---
sidebar_position: 1
---

# disable

### 操作概述

关闭虚拟存储卷缓存服务中io_uring的sqpoll模式

### 命令参数

```bash
-v|--volume-id=string    必要参数，存储卷id，示例：a4ef106e_vs_vol_rep2
```

### 使用示例

```bash
acli storage asan io_uring sqpoll disable -v a4ef106e_vs_vol_rep2
```

### 结果示例

```bash
sqpoll-disable  vol=a4ef106e_vs_vol_rep2  target=interrupt   STATUS: SUCCESS

  HOST               RESULT  DETAIL
  host-002246213d6b  OK      converged
  host-6c92bf51945a  OK      converged

  volume mode: interrupt (persisted)
  hosts: 2/2 converged
```

若卷内某台主机未通过前置检查，则关闭失败并回滚：

```bash
sqpoll-disable  vol=a4ef106e_vs_vol_rep2  target=interrupt   STATUS: FAILED

  HOST               RESULT     DETAIL
  host-002246213d6b  FAILED     precheck: host is in maintenance
  host-6c92bf51945a  REVERTING  applied here, cron will revert

  volume mode: sqpoll (unchanged, not persisted)
  hosts: 1/2 converged
```