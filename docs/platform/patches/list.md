---
sidebar_position: 1
---

# list

### 操作概述

查询本机已打补丁列表

### 命令参数

```bash
-r|--raw=string   是否输出补丁真实名称（剥掉NN-前缀）。0=保留前缀（如01-fix-a），1=剥前缀（如fix-a）。默认='0' 枚举=['0', '1']
```

### 使用示例

```bash
acli platform patches list --raw <string>
```

### 结果示例

默认（保留 NN- 前缀）：

```bash
["01-sp-HCI-6.11.1_R1-c86-col-20260729"]
```

`--raw 1`（剥掉 NN- 前缀）：

```bash
["sp-HCI-6.11.1_R1-c86-col-20260729"]
```
