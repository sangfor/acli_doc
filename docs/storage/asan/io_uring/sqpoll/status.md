---
sidebar_position: 1
---

# status

### 操作概述

查看虚拟存储卷缓存服务中io_uring的sqpoll模式状态

### 命令参数

```bash
-v|--volume-id=string    必要参数，存储卷id，示例：a4ef106e_vs_vol_rep2
```

### 使用示例

```bash
acli storage asan io_uring sqpoll status -v a4ef106e_vs_vol_rep2
```

### 结果示例

sqpoll 模式已开启且卷内主机全部收敛：

```bash
sqpoll-status   vol=a4ef106e_vs_vol_rep2                   STATUS: CONVERGED

  volume: desired=sqpoll  enabled=yes  hosts=3

  HOST               MODE    CONVERGED  KERNEL  SQD CPUS  NOTE
  host-002246213d6b  sqpoll  yes        6.6     70,72
  host-6c92bf51945a  sqpoll  yes        6.6     70,72

  DISKS
    4 disk(s) in sqpoll as expected
```

卷从未配置或主机未收敛时，主机状态与磁盘信息会逐项展开：

```bash
sqpoll-status   vol=a4ef106e_vs_vol_rep2               STATUS: NOT CONVERGED

  volume: desired=<unset>  enabled=no  hosts=2   (never configured)

  HOST               MODE       CONVERGED  KERNEL  SQD CPUS  NOTE
  host-002246213d6b  sqpoll     NO         6.6     70        maintenance
  host-6c92bf51945a  interrupt  yes        5.10    -

  DISKS
    1 disk(s) in interrupt as expected
    host-002246213d6b  nvme0n1  nvme  cdev_iouring  sqpoll  cpu70
```


### 字段说明

| 字段 | 说明 |
| :---: | :--- |
| `desired` | 卷期望模式，`sqpoll` / `interrupt`，未配置时显示 `<unset>` |
| `enabled` | 卷是否已启用 sqpoll（yes/no） |
| `hosts` | 卷内目标主机数量 |
| `MODE` | 主机实际生效模式：sqpoll / interrupt / unknown |
| `CONVERGED` | 期望模式与实际模式是否一致 |
| `KERNEL` | 主机内核版本（仅显示主次版本） |
| `SQD CPUS` | 该主机 sqpoll 独占的 CPU 核 |
| `NOTE` | 主机处于维护模式时显示 `maintenance` |