---
sidebar_position: 1
---

# get

### 操作概述

查看显卡配置文件

### 命令参数

```bash
-n|--name=string    必要参数，显卡配置文件名，示例：gpu_info.ini
```

### 使用示例

```bash
acli hardware gpu config get -n host-005056893c9d_vgpu_load_file.json
```

### 结果示例

```bash
# 模拟数据，以实际为准
{
"gpuname": "Tesla A2000"
}
```
