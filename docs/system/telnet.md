---
sidebar_position: 1
---

# telnet

### 操作概述

探测指定主机和端口的连通性，仅放通只读端口探测形式。

### 命令参数

命令格式：

```bash
acli system telnet <host> <port>
acli system telnet -h
acli system telnet --help
```

支持的参数：

本命令采用封闭式参数白名单（未列举即拒绝）。

```text
<host>      必要参数，目标主机，须满足允许的字符集
<port>      必要参数，目标端口，范围 1-65535
-h|--help   仅允许单独使用，打印帮助信息
```

禁止清单：

探测调用必须恰好包含 `<host> <port>` 两个位置参数。除单独使用的 `-h` 或 `--help` 外，任何以 `-` 开头的选项一律拒绝；额外参数、交互式登录和写类行为均不放通。

### 使用示例

```bash
acli system telnet 127.0.0.1 22
```

### 结果示例

```text
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
Connection closed by foreign host.
```
