---
sidebar_position: 1
---

# scsi_id

### 操作概述

查询 SCSI 设备标识信息，仅执行只读查询，设备路径受控。

### 命令参数

命令格式：

```bash
acli system scsi_id --device=<device> [options]
```

支持的参数：

本命令采用封闭式参数白名单（未列举即拒绝），无写能力。

```text
-g|--whitelisted=flag       将设备视为允许查询的设备
-u|--replace-whitespace=flag 替换输出中的空白字符
-x|--export=flag            以键值形式导出信息
-d|--device=string          指定设备路径，路径须通过访问控制
-p|--page=string            指定要查询的 VPD 页
-s|--sg-version=string      指定 SG 接口版本
```

取值选项支持 `=` 写法，例如 `--device=/dev/sda`。设备须通过 `-d/--device` 选项指定。

禁止清单：

裸位置参数及白名单外选项一律拒绝。

### 使用示例

```bash
acli system scsi_id --device=/dev/sda -g
```

### 结果示例

```text
36000c295698055ee2ad7475a1ee499b2
```
