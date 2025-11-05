---
sidebar_position: 10
---
 
# set
操作概述: 更新loadman服务配置
 
命令参数: 
```bash
-e|--enable=integer           必要参数，是否启用过载保护，枚举值：0(禁用)，1(启用)
-c|--cpu-threshold=integer    必要参数，CPU阈值百分比，范围70-98
```
 
使用示例:
```bash
acli service asv loadman config set -e 1 -c 90
```
 
结果示例:
```bash
cpu_threshold: 90
enabled: 1
```