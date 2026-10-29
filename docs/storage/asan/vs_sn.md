---
sidebar_position: 1
---

# vs_sn

### 操作概述

查询 VS 序列号和机器标识信息，校验序列号完整性、授权限制及一体机签名。

### 命令参数

命令格式：

```bash
acli storage asan vs_sn <option>
```

以下选项说明来自工具帮助：

```text
-f             校验深信服一体机签名
-s [sn keyid]  校验所有 VS 序列号的完整性和授权限制，可指定 sn、keyid
-i             校验所有 VS 序列号的完整性
-u             校验本地 ukey 中 VS 序列号的完整性
-l             打印所有 VS 序列号信息
-p             打印 VS 机器标识
-g             根据序列号和 keyid 打印模块名称
-c             仅校验完整性
-h             打印帮助信息
```

工具帮助的 Usage 行未列出 `-u`，但 Details 中包含该选项；下方保留原始帮助输出。

### 使用示例

```bash
acli storage asan vs_sn
```

### 结果示例

执行 `acli storage asan vs_sn` 返回以下用法提示：

```text
Usage: vs_sn -p|-f|-s|-i|-l|-g|-c|-h
Details:
        -f       verify signature of sangfor fusion-machine
        -s [sn keyid]    verify all vs serial number integrity and authority limit
        -i       verify all vs serial number integrity
        -u       verify local ukey vs serial number integrity
        -l       print all vs serial number info
        -p       print the vs machine id
        -g       print module name from serial number and keyid
        -c       only check integrity
        -h       print help message
```
