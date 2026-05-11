---
sidebar_position: 1
---

# set

### 操作概述

更新loadman服务配置

### 命令参数

```bash
-e|--enabled=integer          必要参数，是否启用过载保护，枚举值：0(禁用)，1(启用)
-c|--cpu-threshold=integer    必要参数，CPU阈值百分比，范围70-98
-m|--master-cores=integer     可选参数，主控节点隔离核数，非负整数，0表示使用系统默认值，最大不超过主机核数的80%
--controller-cores=integer    可选参数，控制节点隔离核数，非负整数，0表示使用系统默认值，最大不超过主机核数的80%
--compute-cores=integer       可选参数，计算节点隔离核数，非负整数，0表示使用系统默认值，最大不超过主机核数的80%
```

### 使用示例

```bash
acli service asv loadman config set -e 1 -c 90 -m 2 --controller-cores 4 --compute-cores 8

acli service asv loadman config set -e 1 -c 90 -m 2
```

### 结果示例

```bash
cpu_threshold: 90
enabled: 1
master_cores: 2
controller_cores: 4
compute_cores: 8
```
