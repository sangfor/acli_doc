---
sidebar_position: 1
---

# list

### 操作概述

查询指定卷的故障域列表

### 命令参数

```bash
-v|--volume-id=string   必要参数，VS卷ID，示例：8a83211f_vs_vol_rep3
-i|--id=string          故障域ID（可选）；传入则只返回该ID的故障域对象，找不到时输出 can not find id <id>；不传则返回所有故障域的JSON数组，示例：1
```

### 使用示例

```bash
acli storage vsmgr fault-domains list --volume-id 8a83211f_vs_vol_rep3
```

### 结果示例

```bash
[
    {
        "name": "domain1",
        "id": 0,
        "hosts": [
            "host-105056913a04",
            "host-105056913a05"
        ]
    },
    {
        "name": "domain2",
        "id": 1,
        "hosts": [
            "host-105056913a06",
            "host-105056913a07"
        ]
    }
]
```

带 `--id` 过滤时只返回单个对象（去掉外层数组）。
