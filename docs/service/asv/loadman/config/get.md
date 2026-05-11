---
sidebar_position: 10
---
 
# get
操作概述: 获取loadman服务配置
 
命令参数: 
```bash
无
```
 
使用示例:
```bash
acli service asv loadman config get
```
 
结果示例:
```bash
cpu_threshold: 90
enabled: 1
master_cores: 2
controller_cores: 4
compute_cores: 8
```

说明: `master_cores`、`controller_cores`、`compute_cores` 的返回值为非负整数，返回 `0` 表示对应节点类型未设置隔离核数。
